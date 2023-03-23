import time
import allure
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.shopping_basket import ShoppingBasket
from pages.sub_category_page import SubCategory
import pytest
import logging
from pytest_zebrunner import attach_test_artifact
import pyscreenrec
from utils.attachments import attach_screenshot, attach_logs, attach_recorded_video
import os


@allure.suite('ShoppingBasket')
class TestShoppingBasket:
    @allure.title('Check usual device price and price in basket')
    def testUsualPriceItemAndInBasket(self, driver):
        start_time = time.time()
        seconds = 0
        recorder = pyscreenrec.ScreenRecorder()
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        recorder.start_recording('recording.mp4', 5)
        main_page.open()
        attach_screenshot()
        main_page.click_universal_category_link(driver, "Смартфони")
        attach_screenshot()
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        attach_screenshot()
        smartphone_price = DeviceCategory.getSmartphonePriceText(self, driver, 1)
        short_characteristics = DeviceCategory.get_goods_title_text_by_index(self, driver, 1)
        DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
        attach_screenshot()
        DeviceCategory.clickOnShoppingBasketButton(self, driver)
        attach_screenshot()
        item_card_description_text = ShoppingBasket.get_goods_description_text_by_index(self, driver, 1)
        assert str(short_characteristics).__contains__(
            item_card_description_text), "Device Short_characteristics not equals"
        shopping_basket_item_price = ShoppingBasket.getDevicePriceText(self, driver, 1)
        assert smartphone_price == shopping_basket_item_price, "Prices are not equals"
        ShoppingBasket.set_goods_count_value(self, driver, 3)
        end_time = time.time()
        attach_recorded_video(self, start_time, end_time, seconds, recorder)
        attach_screenshot()
        smartphone_price_multiply = (smartphone_price * 3)
        time.sleep(2)
        assert smartphone_price_multiply == ShoppingBasket.getSumPriceText(self, driver), "Prices are not equals"
        attach_logs(logging.INFO, 'Test was successful')

    @allure.title('Check if item was added in basket and if empty basket if we remove item')
    def testAddGoodsInBasketAndCheckItEmpty(self, driver):
        start_time = time.time()
        seconds = 0
        recorder = pyscreenrec.ScreenRecorder()
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        recorder.start_recording('recording.mp4', 5)
        main_page.open()
        attach_screenshot()
        main_page.click_universal_category_link(driver, "Смартфони")
        attach_screenshot()
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        attach_screenshot()
        DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
        attach_screenshot()
        DeviceCategory.clickOnShoppingBasketButton(self, driver)
        end_time = time.time()
        attach_recorded_video(self, start_time, end_time, seconds, recorder)
        attach_screenshot()
        assert ShoppingBasket.isBasketEmptyStatusTextPresent(self, driver) == False, \
            "Basket empty status text is presented"
        goods_in_shopping_basket_count = ShoppingBasket.getGoodsInCartListSize(self, driver)
        assert goods_in_shopping_basket_count > 0, "Basket is empty"
        attach_logs(logging.INFO, 'Test was successful')
