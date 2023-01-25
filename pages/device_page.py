from selenium.webdriver.common.by import By
import time
import re


class DevicePage(object):
    def __init__(self, web_driver):
        super().__init__(web_driver)

    def verify_device_short_characteristic(self, driver, param):
        time.sleep(3)
        short_characteristic = driver.find_element(By.XPATH, "//h1[@class='product__title']").text
        return short_characteristic.__contains__(str(param))

    def get_device_short_characteristic(self, driver):
        return driver.find_element(By.XPATH, "//h1[@class='product__title']").text

    def get_chosen_product_price(self, driver):
        chosen_product_price = re.sub('\D', '',
                                      driver.find_element(By.XPATH, "//p[contains(@class,'product-prices__big')]").text)
        return chosen_product_price

    def verifyChosenParameterInShortCharacteristics(self, driver, param):
        time.sleep(3)
        short_characteristic = driver.find_element(By.XPATH, "//p[@class='product-about__brief ng-star-inserted']").text
        return short_characteristic.__contains__(str(param))

    def verifyChosenParamInAllCharacteristics(self, driver, param):
        time.sleep(3)
        short_characteristic = driver.find_element(By.XPATH,
                                                   "//h3[@class='product-tabs__heading']//span[contains(@class,'heading_color_gray')]").text
        return short_characteristic.__contains__(str(param))
