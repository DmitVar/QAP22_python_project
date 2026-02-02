import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    opts = Options()
    # opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1980,1600")
    web_driver = webdriver.Chrome(options=opts)
    yield web_driver
    web_driver.quit()
