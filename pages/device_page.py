from selenium.webdriver.common.by import By
import time
import re

from locators.elements_page_locators import DevicePageLocators
from pages.base_page import BasePage


class DevicePage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)

    def verify_device_short_characteristic(self, driver, param):
        short_characteristic = driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTICS_TITLE).text
        return short_characteristic.__contains__(str(param))

    def get_device_short_characteristic(self, driver):
        return driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTICS_TITLE).text

    def get_chosen_product_price(self, driver):
        time.sleep(3)
        chosen_product_price = re.sub('\D', '', driver.find_element(By.XPATH, DevicePageLocators.PRODUCT_PRICE).text)
        return chosen_product_price

    def verifyChosenParameterInShortCharacteristics(self, driver, param):
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView();",
                              driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTIC))
        short_characteristic = driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTIC).text
        return short_characteristic.__contains__(str(param))

    def verifyChosenParamInAllCharacteristics(self, driver, param):
        short_characteristic = driver.find_element(By.XPATH, DevicePageLocators.ALL_CHARACTERISTIC).text
        return short_characteristic.__contains__(str(param))
