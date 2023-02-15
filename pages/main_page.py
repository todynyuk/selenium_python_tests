from selenium.webdriver.common.by import By
import time

from locators.elements_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_universal_category_link(self, driver, category):
        driver.find_element(By.XPATH, f"//a[@class='menu-categories__link' and contains(.,'{category}')]").click()
        time.sleep(3)

    def set_search_input(self, param):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(param)

    def click_search_button(self):
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()

    def get_goods_title_text(self):
        buffer = self.elements_are_present(self.locators.GOODS_TITLE_TEXTS)
        goods_title_texts = []
        for elem in buffer:
            goods_title_texts.append(elem.text)
        return goods_title_texts

    def verify_is_search_brand_present_in_goods_title(self, brand):
        goods_title_texts = [x.lower() for x in MainPage.get_goods_title_text(self)]
        res = all([ele for ele in str(brand).lower() if (ele in goods_title_texts)])
        return res

    def verify_wrong_search_request(self):
        time.sleep(2)
        return self.element_is_present(self.locators.NOT_FOUND_TEXT).is_displayed()
