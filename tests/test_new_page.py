from playwright.sync_api import Page, expect


def test_new_page(playwright_page: Page):
    playwright_page.goto("https://demoqa.com")
    playwright_page.get_by_role("link", name="Alerts, Frame & Windows").click()
    playwright_page.get_by_role("link", name="Browser Windows").click()

    context = playwright_page.context

    with context.expect_page() as new_page_event:
        playwright_page.get_by_role("button", name="New Tab").click()
        new_page = new_page_event.value

    expect(new_page.locator("h1")).to_have_text("This is a sample page")
