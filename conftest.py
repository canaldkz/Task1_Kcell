import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--force-device-scale-factor=0.8")
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()