from playwright.sync_api import Page, expect


def test_title_main_page(playwright_page: Page):
    """
    Проверка наличия заголовка на главной странице
    Шаги:
        1. Перейти на страницу по адресу http://localhost:3000/
        2. Проверить, что заголовок h2 главной страницы содержит текст Web Automation Torture Labдля автоматизаторов
    Ожидаемый результат:
        1. Заголовок h2 главной страницы содержит текст Web Automation Torture Labдля автоматизаторов
    """
    playwright_page.goto("http://localhost:3000/")
    title = playwright_page.locator("h2")
    expect(title).to_have_text("Web Automation Torture Labдля автоматизаторов")
