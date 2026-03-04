import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def chrome_driver():
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

@pytest.fixture
def firefox_driver():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()