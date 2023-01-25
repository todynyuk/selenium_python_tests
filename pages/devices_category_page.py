from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class DeviceCategory(BasePage):

    def __init__(self, web_driver, url=''):
        url = 'https://rozetka.com.ua/ua/'
        super().__init__(web_driver, url)

    def clear_and_set_sorting_price(self, driver, price_input_type, price_value):
        universal_price_input_value = driver.find_element(By.XPATH,
                                                          "//input[@formcontrolname='%s']" % str(price_input_type))
        universal_price_input_value.clear()
        universal_price_input_value.send_keys(price_value)

    def click_ok_button(self, driver):
        ok_button = driver.find_element(By.XPATH, "//button[contains(@class,'slider-filter__button')]")
        ok_button.click()
        time.sleep(3)

    def get_prices_list(self, driver):
        choosen_price_devices = []
        for elem in driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']"):
            choosen_price_devices.append(re.sub('\D', '', elem.text))
        return choosen_price_devices

    def click_check_box_filter(self, driver, param):
        xpath = f"//a[contains(@data-id,'{param}')]"
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(3)

    def get_goods_title_text(self, driver):
        goods_title_texts = []
        for elem in driver.find_elements(By.XPATH, "//span[@class='goods-tile__title']"):
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
        is_available_status_text_list = driver.find_elements(By.XPATH,
                                                             "//div[contains(@class,'goods-tile__availability') and contains(text(),'%s')]" % str(
                                                                 param))
        for elem in is_available_status_text_list:
            status_text_list.append(elem.text)
        time.sleep(3)
        return status_text_list.__len__()

    def clickDropdownOption(self, driver, param):
        dropDownOption = driver.find_element(By.XPATH,
                                             "//select[contains(@class,'select-css')]/option[contains(text(),'%s')]" % str(
                                                 param))
        dropDownOption.click()
        time.sleep(3)

    def isAllGoodsSortedFromLowToHighPrice(self, driver):
        low_to_hight_price_list = []
        priceItemText = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
        for i in priceItemText:
            low_to_hight_price_list.append(re.sub('\D', '', i.text))
        return all(low_to_hight_price_list[j] <= low_to_hight_price_list[j + 1] for j in
                   range(len(low_to_hight_price_list) - 1))

    def isAllGoodsSortedFromHighToLowPrice(self, driver):
        low_to_hight_price_list = []
        priceItemText = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
        for i in priceItemText:
            low_to_hight_price_list.append(re.sub('\D', '', i.text))
        return all(low_to_hight_price_list[j] >= low_to_hight_price_list[j + 1] for j in
                   range(len(low_to_hight_price_list) - 1))

    def choose_ram_сapacity(self, driver, ram_capacity):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class,'tile-filter__link') and contains(text(),'%s')]" % str(
                    ram_capacity)))).click()

    def getSmartphonePriceText(self, driver, index):
        driver.execute_script("window.scrollTo(0, 220)")
        xpath = f"//span[@class='goods-tile__price-value'][{index}]"
        return int(re.sub('\D', '', driver.find_element(By.XPATH, xpath).text))

    def isAllGoodsSortedFromHighToLowPrice(self, driver):
        low_to_hight_price_list = []
        priceItemText = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
        for i in priceItemText:
            low_to_hight_price_list.append(re.sub('\D', '', i.text))
        return all(low_to_hight_price_list[j] >= low_to_hight_price_list[j + 1] for j in
                   range(len(low_to_hight_price_list) - 1))

    def isAddedToCartGoodsCounterTextPresent(self, driver):
        try:
            driver.find_element(By.XPATH, "//span[contains(@class,'badge--green')]")
        except NoSuchElementException:
            return False
        return True

    def clickBuyButtonByIndex(self, driver, index):
        xpath = f"//button[contains(@class,'buy-button')][{index}]"
        driver.find_element(By.XPATH, xpath).click()

    def clickOnShoppingBasketButton(self, driver):
        shopping_basket_button = driver.find_element(By.XPATH,
                                                     "//li[contains(@class,'cart')]/*/button[contains(@class,'header__button')]")
        shopping_basket_button.click()
        time.sleep(3)

    def clickLinkMoreAboutDevice(self, driver, index):
        driver.execute_script("window.scrollTo(0, 220)")
        xpath = f"//a[@class='goods-tile__heading ng-star-inserted'][{index}]"
        driver.find_element(By.XPATH, xpath).click()

    def clickUniversalShowCheckBoxButton(self, driver, param):
        xpath = f"//span[@class='sidebar-block__toggle-title' and contains (., '{param}')]"
        driver.find_element(By.XPATH, xpath).click()
