from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import pytest
from freezegun import freeze_time


def generate_week_schedule(days_ahead: int = 7, tz: str = "Europe/Helsinki") -> list[tuple[str, str, str]]:
    """
    Генерирует расписание на несколько дней вперёд с учётом часового пояса.

    Для каждого дня формируется кортеж из трёх элементов:
    - сокращённое название дня недели (Mo, Tu, We, Th, Fr, Sa, Su);
    - дата в формате DD/MM;
    - строка с временем работы или значением "Closed" для выходных.

    Логика работы:
    - отсчёт начинается с текущей даты в указанном часовом поясе;
    - для будних дней (понедельник–пятница) время работы фиксировано:
      "00:05–22:55";
    - для выходных (суббота и воскресенье) возвращается "Closed";
    - количество дней определяется параметром `days_ahead`.

    Примеры:
        >>> generate_week_schedule(3, tz="Europe/Helsinki")
        [('Mo', '01/01', '00:05–22:55'),
         ('Tu', '02/01', '00:05–22:55'),
         ('We', '03/01', '00:05–22:55')]

        >>> generate_week_schedule(2, tz="Europe/Helsinki")
        [('Sa', '06/01', 'Closed'),
         ('Su', '07/01', 'Closed')]

    :param days_ahead: Количество дней вперёд, для которых нужно сгенерировать
                       расписание (по умолчанию 7).
    :param tz: Часовой пояс в формате IANA (например, "Europe/Helsinki").
    :return: Список кортежей вида (день_недели, дата, время_работы).
    """
    day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    today = datetime.now(ZoneInfo(tz)).date()
    lst = []
    for i in range(days_ahead):
        d = today + timedelta(days=i)
        wd = d.weekday()  # 0..6
        day_abbr = day_names[wd]
        date_str = d.strftime("%d/%m")
        time_str = "Closed" if wd >= 5 else "00:05–22:55"
        lst.append((day_abbr, date_str, time_str))
    return lst


class TestGenerateWeekSchedule:
    TEST_CASES = [
        (
            "2024-01-01 12:00:00",
            7,
            "Europe/Helsinki",
            [
                ("Mo", "01/01", "00:05–22:55"),
                ("Tu", "02/01", "00:05–22:55"),
                ("We", "03/01", "00:05–22:55"),
                ("Th", "04/01", "00:05–22:55"),
                ("Fr", "05/01", "00:05–22:55"),
                ("Sa", "06/01", "Closed"),
                ("Su", "07/01", "Closed"),
            ],
        ),
        (
            "2024-02-27 12:30:50",
            4,
            "Europe/Helsinki",
            [
                ("Tu", "27/02", "00:05–22:55"),
                ("We", "28/02", "00:05–22:55"),
                ("Th", "29/02", "00:05–22:55"),
                ("Fr", "01/03", "00:05–22:55"),
            ],
        ),
        (
            "2025-02-28 12:00:00",
            3,
            "Europe/Helsinki",
            [("Fr", "28/02", "00:05–22:55"), ("Sa", "01/03", "Closed"), ("Su", "02/03", "Closed")],
        ),
        (
            "2024-01-06 12:00:00",
            4,
            "Europe/Helsinki",
            [
                ("Sa", "06/01", "Closed"),
                ("Su", "07/01", "Closed"),
                ("Mo", "08/01", "00:05–22:55"),
                ("Tu", "09/01", "00:05–22:55"),
            ],
        ),
        ("2024-01-01 12:00:00", -1, "Europe/Helsinki", []),
        ("2024-01-01 10:00:00", 1, "Pacific/Auckland", [("Mo", "01/01", "00:05–22:55")]),
        ("2024-01-01 12:00:00", 2, "Asia/Tokyo", [("Mo", "01/01", "00:05–22:55"), ("Tu", "02/01", "00:05–22:55")]),
    ]

    @pytest.mark.parametrize("freeze_time_date, days_ahead, tz, expected", TEST_CASES)
    def test_generate_week_schedule_function(self, freeze_time_date, days_ahead, tz, expected):
        with freeze_time(freeze_time_date):
            actual = generate_week_schedule(days_ahead=days_ahead, tz=tz)
            assert actual == expected

    @pytest.mark.parametrize(
        "freeze_time_date, days_ahead, tz, error_type",
        [
            ("2024-01-01 12:00:00", 1, "Invalid/Timezone", ZoneInfoNotFoundError),
            ("2024-01-01 12:00:00", 1, "", ValueError),
            ("2024-01-01 12:00:00", None, "Europe/Helsinki", TypeError),
            ("2024-01-01 12:00:00", "7", "Europe/Helsinki", TypeError),
        ],
    )
    def test_negative_generate_week_schedule_function(self, freeze_time_date, days_ahead, tz, error_type):
        with freeze_time("2024-01-01 12:00:00"):
            with pytest.raises(error_type):
                generate_week_schedule(days_ahead=days_ahead, tz=tz)
