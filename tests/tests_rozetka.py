import time

from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.shopping_basket import ShoppingBasket
from pages.sub_category_page import SubCategory


class TestRozetkaFilters:
    class TestsRozetka:

        def test_correct_main_search(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            search_text = "Agm A9"
            main_page.set_search_input(search_text)
            main_page.click_search_button()
            assert main_page.verify_is_search_brand_present_in_goods_title(search_text), "Search text not" \
                                                                                         " contains in all " \
                                                                                         "goods title texts"

        def test_uncorrect_main_search(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            search_text = "hgvhvg"
            main_page.set_search_input(search_text)
            main_page.click_search_button()
            assert main_page.verify_wrong_search_request(), "Wrong request text isn`t presented"

    class TestDevicesCategoryPage:

        def testSearchBrandNameMaxCustomPriceAndAvailable(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            main_page.click_universal_category_link(driver, "Смартфони")
            time.sleep(2)
            SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
            assert str(driver.title).lower().__contains__(("Мобільні").lower())
            DeviceCategory.clear_and_set_sorting_price(self, driver, "max", 4000)
            DeviceCategory.click_ok_button(self, driver)
            assert DeviceCategory.check_is_all_goods_prices_less_than_choosen(self, driver, 4000), \
                "One or more things have price more than choosen"
            DeviceCategory.click_check_box_filter(self, driver, "Sigma")
            assert DeviceCategory.verify_is_search_think_present_in_goods_title(self, driver, "Sigma"), \
                "Search result don`t contains chosen brand"
            DeviceCategory.click_check_box_filter(self, driver, "Є в наявності")
            length = DeviceCategory.check_is_all_goods_available(self, driver, "Немає в наявності")
            assert length == 0, "One or more goods are not available"

        def testVerifyItemRamMatrixTypeAndProcessor(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            main_page.click_universal_category_link(driver, "Ноутбуки")
            SubCategory.click_universal_subcategory_menu_link(self, "моноблоки", driver)
            DeviceCategory.click_check_box_filter(self, driver, "Intel Core i5")
            DeviceCategory.click_check_box_filter(self, driver, "Моноблок")
            DeviceCategory.click_check_box_filter(self, driver, "8 ГБ")
            DeviceCategory.clickUniversalShowCheckBoxButton(self, driver, "Тип матриці")
            DeviceCategory.click_check_box_filter(self, driver, "IPS")
            DeviceCategory.click_check_box_filter(self, driver, "Новий")
            DeviceCategory.click_check_box_filter(self, driver, "Є в наявності")
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

        def testVerifySortByPrice(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            main_page.click_universal_category_link(driver, "Смартфони")
            SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
            DeviceCategory.clickDropdownOption(self, driver, "Від дешевих до дорогих")
            is_good_prices_low_to_hight = DeviceCategory.isAllGoodsSortedFromLowToHighPrice(self, driver)
            assert is_good_prices_low_to_hight, "One or more prices not sorted from low to high price"
            DeviceCategory.clickDropdownOption(self, driver, "Від дорогих до дешевих")
            is_good_prices_hight_to_low = DeviceCategory.isAllGoodsSortedFromHighToLowPrice(self, driver)
            assert is_good_prices_hight_to_low, "One or more prices not sorted from high to low price"

        def testAddingAndCountGoodsInBasket(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            main_page.click_universal_category_link(driver, "Смартфони")
            SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
            assert DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, driver) == False, \
                "Cart Goods Counter Text isn't presented"

            DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
            assert DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, driver) != False, \
                "Cart Goods Counter Text isn't presented"

    class TestDevicePage:
        def testItemRamAndPrice(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            main_page.click_universal_category_link(driver, "Смартфони")
            SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
            DeviceCategory.choose_ram_сapacity(self, driver, 12)
            DeviceCategory.click_check_box_filter(self, driver, "Синій")  # not click
            smartphone_price = DeviceCategory.getSmartphonePriceText(self, driver, 1)
            DeviceCategory.clickLinkMoreAboutDevice(self, driver, 1)
            short_characteristics = DevicePage.verify_device_short_characteristic(self, driver, 12)
            chosen_device_price = DevicePage.get_chosen_product_price(self, driver)
            assert short_characteristics, "Short_characteristics don't contains chosen ram capacity"
            assert str(smartphone_price) == chosen_device_price, "Prices are not equals"

    class TestShoppingBasket:

        def testUsualPriceItemAndInBasket(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            main_page.click_universal_category_link(driver, "Смартфони")
            SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
            smartphone_price = DeviceCategory.getSmartphonePriceText(self, driver, 1)
            short_characteristics = DeviceCategory.get_goods_title_text_by_index(self, driver, 1)
            DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
            DeviceCategory.clickOnShoppingBasketButton(self, driver)
            item_card_description_text = ShoppingBasket.get_goods_description_text_by_index(self, driver, 1)
            assert str(short_characteristics).__contains__(
                item_card_description_text), "Device Short_characteristics not equals"
            shopping_basket_item_price = ShoppingBasket.getDevicePriceText(self, driver, 1)
            assert smartphone_price == shopping_basket_item_price, "Prices are not equals"
            ShoppingBasket.set_goods_count_value(self, driver, 3)
            smartphone_price_multiply = (smartphone_price * 3)
            time.sleep(2)
            assert smartphone_price_multiply == ShoppingBasket.getSumPriceText(self, driver), "Prices are not equals"

        def testAddGoodsInBasketAndCheckItEmpty(self, driver):
            main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
            main_page.open()
            main_page.click_universal_category_link(driver, "Смартфони")
            SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
            DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
            DeviceCategory.clickOnShoppingBasketButton(self, driver)
            assert ShoppingBasket.isBasketEmptyStatusTextPresent(self, driver) == False, \
                "Basket empty status text is presented"
            goods_in_shopping_basket_count = ShoppingBasket.getGoodsInCartListSize(self, driver)
            assert goods_in_shopping_basket_count > 0, "Basket is empty"
