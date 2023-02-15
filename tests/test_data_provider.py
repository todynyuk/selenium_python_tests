import self
import pytest
from selenium import webdriver
from pages.main_page import MainPage
from utils import get_excel_data

brands_list = get_excel_data.get_data()


@pytest.mark.parametrize("brand", brands_list)
def test_data_provider_search_brand(brand):
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    web_driver.get("https://rozetka.com.ua/ua/")
    MainPage.set_search_input(self, web_driver, brand)
    MainPage.click_search_button(self, web_driver)
    assert MainPage.verify_is_search_brand_present_in_goods_title(self, web_driver, brand)
    web_driver.close()
