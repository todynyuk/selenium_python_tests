import time
import allure
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.sub_category_page import SubCategory
import pytest
import logging
import pyscreenrec
from utils.attachments import attach_screenshot, attach_logs, attach_recorded_video
import os


@allure.suite('DevicesCategory')
class TestDevicesCategoryPage:

    @pytest.mark.skip(reason="Rozetka have problem with sorting by price")
    @allure.title('Check filter by BrandName,MaxCustomPrice,and available')
    def testFilterByBrandNameMaxCustomPriceAndAvailable(self, driver):
        os.remove("../recording.mp4")
        start_time = time.time()
        seconds = 0
        recorder = pyscreenrec.ScreenRecorder()
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        recorder.start_recording('recording.mp4', 5)
        main_page.open()
        attach_screenshot()
        main_page.click_universal_category_link(driver, "Смартфони")
        time.sleep(2)
        attach_screenshot()
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        assert str(driver.title).lower().__contains__(("Мобільні").lower())
        DeviceCategory.clear_and_set_sorting_price(self, driver, "max", 4000)
        DeviceCategory.click_ok_button(self, driver)
        attach_screenshot()
        assert DeviceCategory.check_is_all_goods_prices_less_than_choosen(self, driver, 4000), \
            "One or more things have price more than choosen"
        DeviceCategory.click_check_box_filter(self, driver, "Sigma")
        attach_screenshot()
        assert DeviceCategory.verify_is_search_think_present_in_goods_title(self, driver, "Sigma"), \
            "Search result don`t contains chosen brand"
        DeviceCategory.click_check_box_filter(self, driver, "Є в наявності")
        end_time = time.time()
        attach_recorded_video(self, start_time, end_time, seconds, recorder)
        attach_screenshot()
        length = DeviceCategory.check_is_all_goods_available(self, driver, "Немає в наявності")
        assert length == 0, "One or more goods are not available"
        attach_logs(logging.INFO, 'Test was successful')

    @allure.title('Check filter by ram,matrix type and processor')
    def testVerifyItemRamMatrixTypeAndProcessor(self, driver):
        start_time = time.time()
        seconds = 0
        recorder = pyscreenrec.ScreenRecorder()
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        recorder.start_recording('recording.mp4', 5)
        main_page.open()
        attach_screenshot()
        main_page.click_universal_category_link(driver, "Ноутбуки")
        attach_screenshot()
        SubCategory.click_universal_subcategory_menu_link(self, "моноблоки", driver)
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "Intel Core i5")
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "Моноблок")
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "8 ГБ")
        attach_screenshot()
        DeviceCategory.clickUniversalShowCheckBoxButton(self, driver, "Тип матриці")
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "IPS")
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "Новий")
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "Є в наявності")
        attach_screenshot()
        length = DeviceCategory.check_is_all_goods_available(self, driver,
                                                             "Немає в наявності")
        assert length == 0, "One or more goods are not available"
        DeviceCategory.clickLinkMoreAboutDevice(self, driver, 1)
        assert DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, "Intel Core i5"), \
            "Processor name text not contains in about device text"
        assert DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, "8 ГБ"), \
            "Ram text not contains in about device text"
        assert DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, "IPS"), \
            "Matrix type text not contains in about device text"
        assert DevicePage.verifyChosenParamInAllCharacteristics(self, driver,
                                                                "Моноблок"), "Computer type text not contains in description device text"
        end_time = time.time()
        attach_recorded_video(self, start_time, end_time, seconds, recorder)
        attach_logs(logging.INFO, 'Test was successful')

    @pytest.mark.skip(reason="Rozetka have problem with sorting by price")
    @allure.title('Check filter by price')
    def testVerifySortByPrice(self, driver):
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
        DeviceCategory.clickDropdownOption(self, driver, "Від дешевих до дорогих")
        attach_screenshot()
        is_good_prices_low_to_hight = DeviceCategory.isAllGoodsSortedFromLowToHighPrice(self, driver)
        assert is_good_prices_low_to_hight, "One or more prices not sorted from low to high price"
        DeviceCategory.clickDropdownOption(self, driver, "Від дорогих до дешевих")
        end_time = time.time()
        attach_recorded_video(self, start_time, end_time, seconds, recorder)
        attach_screenshot()
        is_good_prices_hight_to_low = DeviceCategory.isAllGoodsSortedFromHighToLowPrice(self, driver)
        assert is_good_prices_hight_to_low, "One or more prices not sorted from high to low price"
        attach_logs(logging.INFO, 'Test was successful')

    @allure.title('Check adding items to basket and basket goods counter')
    def testAddingAndCountGoodsInBasket(self, driver):
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
        assert DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, driver) == False, \
            "Cart Goods Counter Text isn't presented"

        DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
        end_time = time.time()
        attach_recorded_video(self, start_time, end_time, seconds, recorder)
        assert DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, driver) != False, \
            "Cart Goods Counter Text isn't presented"
        attach_logs(logging.INFO, 'Test was successful')

    @allure.title('Check filter by BrandName')
    def test_choose_brands_and_check(self, driver):
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
        DeviceCategory.click_check_box_filter(self, driver, "Huawei")
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "Infinix")
        attach_screenshot()
        DeviceCategory.click_check_box_filter(self, driver, "Motorola")
        end_time = time.time()
        attach_recorded_video(self, start_time, end_time, seconds, recorder)
        attach_screenshot()
        assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self, driver, "Huawei"), \
            "List chosen parameters not contains this parameter"
        assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self, driver, "Infinix"), \
            "List chosen parameters not contains this parameter"
        assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self, driver, "Motorola"), \
            "List chosen parameters not contains this parameter"
        attach_logs(logging.INFO, 'Test was successful')
