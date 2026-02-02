import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture
def page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
