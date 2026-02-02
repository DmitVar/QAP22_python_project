import pytest


def format_price(price: str) -> str:
    """
    Форматирует строковое представление цены в человекочитаемый вид.

    Функция:
    - пытается преобразовать входное значение в число (`float`);
    - округляет значение до двух знаков после запятой;
    - разделяет целую часть на группы по три цифры с пробелом;
    - всегда использует точку как десятичный разделитель.

    Если входное значение нельзя преобразовать в число (например, это
    не строка или строка не является числом), функция возвращает его
    без изменений.

    Примеры:
        >>> format_price("1234")
        '1 234.00'
        >>> format_price("1234567.8")
        '1 234 567.80'
        >>> format_price("99.999")
        '100.00'
        >>> format_price("abc")
        'abc'
        >>> format_price(None)
        None

    :param price: Цена в виде строки, содержащей числовое значение.
    :return: Отформатированная строка цены или исходное значение,
             если форматирование невозможно.
    """

    try:
        price_float = float(price)
        price_str = f"{price_float:.2f}"
        integer_part, decimal_part = price_str.split(".")
        formatted_parts = []
        for i in range(len(integer_part), 0, -3):
            start = max(0, i - 3)
            formatted_parts.insert(0, integer_part[start:i])
        return " ".join(formatted_parts) + "." + decimal_part
    except (ValueError, AttributeError):
        return price


@pytest.mark.parametrize(
    "input_str, expected_str",
    [
        ("1234.567", "1 234.57"),
        ("999.999", "1 000.00"),
        ("0.99", "0.99"),
        ("1234567890.123456", "1 234 567 890.12"),
        ("999", "999.00"),
        ("-1234.56", "-1 234.56"),
        ("  1234.56  ", "1 234.56"),
        ("20198,98", "20 198.98"),
        ("12a125", "12a125"),
        ("12125.1a2", "12125.1a2"),
        ("12125.12b", "12125.12b"),
        ("0.999", "1.00"),
    ],
)
def test_format_price_function(input_str, expected_str):
    assert format_price(input_str) == expected_str
