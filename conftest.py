import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pytest_plugins = ("fixtures.pages",)


@pytest.fixture()
def driver():
    opts = Options()
    # opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1980,1600")
    opts.add_argument("--incognito")
    web_driver = webdriver.Chrome(options=opts)
    web_driver.implicitly_wait(15)
    yield web_driver
    web_driver.quit()
