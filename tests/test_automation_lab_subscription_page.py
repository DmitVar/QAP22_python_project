import pytest

smoke_test_cases_promo_code = [
    ("BASIC199", "base", "1_month", "Промокод применён: Специальная цена 199₷/мес на Базовый тариф"),
    ("BASIC199", "premium", "1_month", "Промокод только для: Базовый"),
    ("WELCOME10", "base", "1_month", "Промокод истек 31.12.2024"),
    ("FAMILY300", "family", "3_months", "Промокод истек 30.06.2024"),
    ("ALWAYS", "base", "12_months", "Промокод применён: Скидка 15% для для всех тарифов"),
    ("ALWAYS", "base", "1_month", "Минимальная сумма для промокода: 300₷"),
    ("DIMA2026", "premium", "3_months", "Промокод не найден"),
]


class TestAutomationLabSubscriptionPage:

    @pytest.mark.parametrize("promo_code, tariff, period, expected", smoke_test_cases_promo_code)
    def test_check_promo_code(self, page, promo_code, tariff, period, expected):
        page.goto("http://localhost:3000/automation-lab/subscription")
        period_1_button = page.locator('[data-testid="period-1"]')
        period_3_button = page.locator('[data-testid="period-3"]')
        period_12_button = page.locator('[data-testid="period-12"]')
        basic_tariff_card = page.locator('[data-testid="tariff-basic"]')
        premium_tariff_card = page.locator('[data-testid="tariff-premium"]')
        family_tariff_card = page.locator('[data-testid="tariff-family"]')

        match period:
            case "1_month":
                period_1_button.click()
            case "3_months":
                period_3_button.click()
            case "12_months":
                period_12_button.click()

        match tariff:
            case "base":
                basic_tariff_card.click()
            case "premium":
                premium_tariff_card.click()
            case "family":
                family_tariff_card.click()

        promo_code_input = page.locator('[data-testid="promo-input"]')
        promo_code_input.clear()
        promo_code_input.fill(promo_code)

        apply_promo_button = page.locator('[data-testid="promo-apply-btn"]')
        apply_promo_button.click()
        promo_message_result = page.locator('[data-testid="promo-message"]')
        actual_message = promo_message_result.text_content()
        assert actual_message == expected

    def test_add_card(self, page):
        page.goto("http://localhost:3000/automation-lab/subscription")
        card_number_input = page.locator('[data-testid="card-number"]')
        card_number_input.clear()
        card_number_input.fill("4111 1111 1111 1111")
        validity_period_input = page.locator('[data-testid="card-expiry"]')
        validity_period_input.clear()
        validity_period_input.fill("0930")
        cvv_card_input = page.locator('[data-testid="card-cvv"]')
        cvv_card_input.clear()
        cvv_card_input.fill("333")
        pay_button = page.locator('[data-testid="pay-button"]')
        pay_button.click()
        popup_title = page.locator("div.success-modal h3")
        popup_title_text = popup_title.text_content()
        assert popup_title_text == "Успешно!"
