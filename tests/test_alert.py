from playwright.sync_api import Dialog, Page, expect


def test_alert(playwright_page: Page):
    playwright_page.goto("https://demoqa.com")

    def accept_dialog(dialog: Dialog):
        dialog.accept()

    playwright_page.on("dialog", accept_dialog)
    playwright_page.get_by_role("link", name="Alerts, Frame & Windows").click()
    playwright_page.get_by_role("link", name="Alerts").click()
    expect(playwright_page.locator("h1")).to_have_text("Alerts")
    button = playwright_page.locator("#alertButton")
    expect(button).to_be_enabled()

    with playwright_page.expect_event("dialog"):
        button.click()
