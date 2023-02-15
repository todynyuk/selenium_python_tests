from selenium.webdriver.common.by import By
import time
import re
from selenium.common.exceptions import NoSuchElementException


class ShoppingBasket(object):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def get_goods_description_text_by_index(self, driver, index):
        xpath = f"//a[@data-testid='title'][{index}]"
        goods_title_text = driver.find_element(By.XPATH, xpath).text
        return goods_title_text

    def getDevicePriceText(self, driver, index):
        xpath = f"//p[@data-testid='cost'][{index}]"
        return int(re.sub('\D', '', driver.find_element(By.XPATH, xpath).text))

    def set_goods_count_value(self, driver, count):
        universal_price_input_value = driver.find_element(By.XPATH,
                                                          "//input[@data-testid='cart-counter-input']")
        universal_price_input_value.clear()
        time.sleep(2)
        universal_price_input_value.send_keys(count)

    def getSumPriceText(self, driver):
        return int(
            re.sub('\D', '', driver.find_element(By.XPATH, "//div[@class='cart-receipt__sum-price']//span").text))

    def isBasketEmptyStatusTextPresent(self, driver):
        try:
            time.sleep(2)
            driver.find_element(By.XPATH, "//h4[@class='cart-dummy__heading']")
            time.sleep(2)
        except NoSuchElementException:
            time.sleep(2)
            return False
        return True

    def getGoodsInCartListSize(self, driver):
        goods_in_cart_title_price = []
        for elem in driver.find_elements(By.XPATH, "//p[@data-testid='cost']"):
            goods_in_cart_title_price.append(elem.text)
        return goods_in_cart_title_price.__len__()
