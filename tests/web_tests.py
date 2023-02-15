import time
from pages.base_page import BasePage
import pytest
from selenium import webdriver
from time import sleep




@pytest.mark.parametrize('input_browser, input_url',
                         [
                             ('chrome', 'http://www.lambdatest.com'),
                             ('chrome', 'http://www.duckduckgo.com'),
                             ('chrome', 'http://www.google.com'),
                         ]
                         )
def test_url_on_browsers(input_browser, input_url):
    if input_browser == "chrome":
        web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    web_driver.get(input_url)
    print(web_driver.title)
    sleep(5)
    web_driver.close()

def test(driver):
    page = BasePage(driver, 'https://google.com')
    page.open()
    time.sleep(3)
