from selenium.webdriver.common.by import By
import time

from locators.elements_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def __init__(self, web_driver, url=''):
        url = 'https://rozetka.com.ua/ua/'
        super().__init__(web_driver, url)

    def click_universal_category_link(self, category, driver):
        driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'%s')]" % str(
            category)).click()
        time.sleep(3)

    def set_search_input(self, driver, param):
        driver.find_element(By.CSS_SELECTOR, "input[name='search']").send_keys(param)

    def click_search_button(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class,'button_color_green')]").click()

    def get_goods_title_text(self, driver):
        goods_title_texts = []
        for elem in driver.find_elements(By.XPATH, "//span[@class='goods-tile__title']"):
            goods_title_texts.append(elem.text)
        return goods_title_texts

    def verify_is_search_brand_present_in_goods_title(self, driver, brand):
        goods_title_texts = [x.lower() for x in MainPage.get_goods_title_text(self, driver)]
        res = all([ele for ele in str(brand).lower() if (ele in goods_title_texts)])
        return res

    def verify_wrong_search_request(self, driver):
        time.sleep(2)
        return driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").is_displayed()
