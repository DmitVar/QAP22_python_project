from playwright.sync_api import Page


def test_alert(playwright_page: Page):
    playwright_page.goto("https://demoqa.com")

    playwright_page.get_by_role("link", name="Alerts, Frame & Windows").click()
    playwright_page.get_by_role("link", name="Frames", exact=True).click()
    frame = playwright_page.frame_locator("#frame1")
    frame_title = frame.locator("h1").inner_text()
    assert frame_title == "This is a sample page"
