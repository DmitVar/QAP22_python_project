import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture
def playwright_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
