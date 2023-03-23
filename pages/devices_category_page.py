from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from locators.elements_page_locators import DeviceCategoryLocators
from pages.base_page import BasePage


class DeviceCategory(BasePage):
    locators = DeviceCategoryLocators()

    def clear_and_set_sorting_price(self, driver, price_input_type, price_value):
        universal_price_input_value = driver.find_element(By.XPATH,
                                                          f"//input[@formcontrolname='{price_input_type}']")
        universal_price_input_value.clear()
        universal_price_input_value.send_keys(price_value)

    def click_ok_button(self, driver):
        driver.find_element(By.XPATH, DeviceCategoryLocators.OK_BUTTON).click()
        time.sleep(3)

    def get_prices_list(self, driver):
        choosen_price_devices = []
        for elem in driver.find_elements(By.XPATH, DeviceCategoryLocators.DEVICE_PRICES):
            choosen_price_devices.append(re.sub('\D', '', elem.text))
        return choosen_price_devices

    def click_check_box_filter(self, driver, param):
        element = driver.find_element(By.XPATH, f"//a[contains(@data-id,'{param}')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element.click()
        time.sleep(3)

    def get_goods_title_text(self, driver):
        goods_title_texts = []
        for elem in driver.find_elements(By.XPATH, DeviceCategoryLocators.GOODS_TITLE_TEXT):
            goods_title_texts.append(elem.text)
        return goods_title_texts

    def check_is_all_goods_prices_less_than_choosen(self, driver, chosen_max_price):
        return all(int(i) <= int(chosen_max_price) for i in DeviceCategory.get_prices_list(self, driver))

    def verify_is_search_think_present_in_goods_title(self, driver, think_name):
        goods_title_texts = [x.lower() for x in DeviceCategory.get_goods_title_text(self, driver)]
        res = all([ele for ele in str(think_name).lower() if (ele in goods_title_texts)])
        return res

    def get_goods_title_text_by_index(self, driver, index):
        xpath = f"//span[@class='goods-tile__title'][{index}]"
        goods_title_text = driver.find_element(By.XPATH, xpath).text
        return goods_title_text

    def check_is_all_goods_available(self, driver, param):
        status_text_list = []
        driver.execute_script("window.scrollTo(0, 220)")
        is_available_status_text_list = driver.find_elements(By.XPATH,
                                                             f"//div[contains(@class,'goods-tile__availability') and "
                                                             f"contains(text(),'{param}')]")
        for elem in is_available_status_text_list:
            status_text_list.append(elem.text)
        time.sleep(3)
        return status_text_list.__len__()

    def clickDropdownOption(self, driver, param):
        dropDownOption = driver.find_element(By.XPATH,
                                             f"//select[contains(@class,'select-css')]/option[contains(text(),"
                                             f"'{param}')]")
        dropDownOption.click()
        time.sleep(3)

    def isAllGoodsSortedFromLowToHighPrice(self, driver):
        low_to_hight_price_list = []
        priceItemText = driver.find_elements(By.XPATH, DeviceCategoryLocators.DEVICE_PRICES)
        for i in priceItemText:
            low_to_hight_price_list.append(re.sub('\D', '', i.text))
        return all(low_to_hight_price_list[j] <= low_to_hight_price_list[j + 1] for j in
                   range(len(low_to_hight_price_list) - 1))

    def isAllGoodsSortedFromHighToLowPrice(self, driver):
        low_to_hight_price_list = []
        priceItemText = driver.find_elements(By.XPATH, DeviceCategoryLocators.DEVICE_PRICES)
        for i in priceItemText:
            low_to_hight_price_list.append(re.sub('\D', '', i.text))
        return all(low_to_hight_price_list[j] >= low_to_hight_price_list[j + 1] for j in
                   range(len(low_to_hight_price_list) - 1))

    def choose_ram_сapacity(self, driver, ram_capacity):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[contains(@class,'tile-filter__link') and contains(text(),'{ram_capacity}')]"))).click()

    def getSmartphonePriceText(self, driver, index):
        driver.execute_script("window.scrollTo(0, 220)")
        xpath = f"//span[@class='goods-tile__price-value'][{index}]"
        return int(re.sub('\D', '', driver.find_element(By.XPATH, xpath).text))

    def isAllGoodsSortedFromHighToLowPrice(self, driver):
        low_to_hight_price_list = []
        priceItemText = driver.find_elements(By.XPATH, DeviceCategoryLocators.DEVICE_PRICES)
        for i in priceItemText:
            low_to_hight_price_list.append(re.sub('\D', '', i.text))
        return all(low_to_hight_price_list[j] >= low_to_hight_price_list[j + 1] for j in
                   range(len(low_to_hight_price_list) - 1))

    def isAddedToCartGoodsCounterTextPresent(self, driver):
        try:
            time.sleep(2)
            driver.find_element(By.XPATH, DeviceCategoryLocators.CART_GOODS_COUNTER_TEXT)
        except NoSuchElementException:
            return False
        return True

    def clickBuyButtonByIndex(self, driver, index):
        driver.execute_script("window.scrollTo(0, 250)")
        time.sleep(2)
        element = driver.find_element(By.XPATH, f"//button[contains(@class,'buy-button')][{index}]")
        element.click()

    def clickOnShoppingBasketButton(self, driver):
        shopping_basket_button = driver.find_element(By.XPATH, DeviceCategoryLocators.SHOPPING_BASKET_BUTTON)
        shopping_basket_button.click()
        time.sleep(3)

    def clickLinkMoreAboutDevice(self, driver, index):
        driver.execute_script("window.scrollTo(0, 220)")
        xpath = f"//a[@class='goods-tile__heading ng-star-inserted'][{index}]"
        driver.find_element(By.XPATH, xpath).click()

    def clickUniversalShowCheckBoxButton(self, driver, param):
        xpath = f"//span[@class='sidebar-block__toggle-title' and contains (., '{param}')]"
        driver.find_element(By.XPATH, xpath).click()

    def go_to_up_page(self, driver):
        driver.execute_script("window.scrollTo(0, 220)")

    def check_chosen_filters_contains_chosen_brands(self, driver, chosen_brand):
        chosen_filters = []
        chosen_filtersText = driver.find_elements(By.XPATH, DeviceCategoryLocators.FILTER_LINKS)
        for i in chosen_filtersText:
            chosen_filters.append(str(i.text).replace(' ', ''))
        return chosen_filters.__contains__(chosen_brand)
