import time
import allure
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.shopping_basket import ShoppingBasket
from pages.sub_category_page import SubCategory
import pytest
import logging
from pytest_zebrunner import attach_test_artifact, attach_test_screenshot
import pyscreenrec
from utils.attachments import attach_screenshot, attach_logs, attach_recorded_video


@allure.suite('RozetkaFilters')
class TestRozetkaFilters:
    @allure.feature('MainPage')
    class TestsRozetkaMainPageSearch:

        @pytest.mark.label("Search", "correct")
        @allure.title('Check correct search')
        def test_correct_search(self, driver):
            start_time = time.time()
            seconds = 0
            recorder = pyscreenrec.ScreenRecorder()
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            recorder.start_recording('recording.mp4', 5)
            main_page.open()
            attach_screenshot()
            search_text = "Agm A9"
            main_page.set_search_input(search_text)
            main_page.click_search_button()
            end_time = time.time()
            attach_recorded_video(self, start_time, end_time, seconds, recorder)
            attach_test_artifact("recording.mp4")
            attach_screenshot()
            attach_logs(logging.INFO, 'Test was successful')
            assert main_page.verify_is_search_brand_present_in_goods_title(search_text), "Search text not" \
                                                                                         " contains in all " \
                                                                                         "goods title texts"

        @allure.title('Check incorrect search')
        def test_incorrect_search(self, driver):
            start_time = time.time()
            seconds = 0
            recorder = pyscreenrec.ScreenRecorder()
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            recorder.start_recording('recording.mp4', 5)
            main_page.open()
            attach_screenshot()
            search_text = "hgvhvg"
            main_page.set_search_input(search_text)
            main_page.click_search_button()
            end_time = time.time()
            attach_recorded_video(self, start_time, end_time, seconds, recorder)
            attach_screenshot()
            attach_logs(logging.INFO, 'Test was successful')
            assert main_page.verify_wrong_search_request(), "Wrong request text isn`t presented"

    @allure.feature('DevicesCategory')
    class TestDevicesCategoryPage:

        @allure.title('Check filter by BrandName,MaxCustomPrice,and available')
        def testFilterByBrandNameMaxCustomPriceAndAvailable(self, driver):
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
                "Processor name text not contains in about device text"#test was failed it this line
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
            assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self,driver, "Huawei"), \
                "List chosen parameters not contains this parameter"
            assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self,driver, "Infinix"), \
                "List chosen parameters not contains this parameter"
            assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self,driver, "Motorola"), \
                "List chosen parameters not contains this parameter"
            attach_logs(logging.INFO, 'Test was successful')

    @allure.feature('DevicePage')
    class TestDevicePage:
        @allure.title('Check verify in chosen device ram and price')
        def testItemRamAndPrice(self, driver):
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
            DeviceCategory.choose_ram_сapacity(self, driver, 12)
            attach_screenshot()
            DeviceCategory.click_check_box_filter(self, driver, "Синій")
            attach_screenshot()
            smartphone_price = DeviceCategory.getSmartphonePriceText(self, driver, 1)
            DeviceCategory.clickLinkMoreAboutDevice(self, driver, 1)
            attach_screenshot()
            short_characteristics = DevicePage.verify_device_short_characteristic(self, driver, 12)
            end_time = time.time()
            attach_recorded_video(self, start_time, end_time, seconds, recorder)
            chosen_device_price = DevicePage.get_chosen_product_price(self, driver)
            assert short_characteristics, "Short_characteristics don't contains chosen ram capacity"
            assert str(smartphone_price) == chosen_device_price, "Prices are not equals"
            attach_logs(logging.INFO, 'Test was successful')

    @allure.feature('ShoppingBasket')
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
