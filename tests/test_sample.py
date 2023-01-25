import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.shopping_basket import ShoppingBasket
from pages.sub_category_page import SubCategory
from pages.devices_category_page import DeviceCategory
from pages.device_page import DevicePage


class PythonTestSample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_rozetka(self):
        driver = self.driver
        driver.get("https://rozetka.com.ua/ua/")
        driver.maximize_window()
        self.assertIn("ROZETKA", driver.title)
        elem = driver.find_element(By.XPATH, "//input[contains(@class, 'search-form__input')]")
        search_input = elem.is_displayed()
        search_input1 = elem.is_enabled()
        assert search_input, 'element not displayed'
        assert search_input1, 'element not enabled'
        assert "No results found." not in driver.page_source

    def main_part(self):
        driver = self.driver
        driver.get("https://rozetka.com.ua/ua/")
        driver.maximize_window()
        self.category = "Смартфони"
        self.sub_category = "Мобільні"
        self.price_input_type = "max"
        self.price_value = 4000
        self.brand_name = "Sigma"
        self.is_available = "Є в наявності"
        self.not_available = "Немає в наявності"
        self.cheap = "Від дешевих до дорогих"
        self.expensive = "Від дорогих до дешевих"
        self.ram_capacity = 12
        self.color = "Синій"
        self.index = 1
        self.count = 3
        MainPage.click_universal_category_link(self, self.category, driver)
        SubCategory.click_universal_subcategory_menu_link(self, self.sub_category, driver)

    def testVerifySearchBrandNameMaxCustomPriceAndAvailable(self):
        self.main_part()
        self.assertTrue(str(self.driver.title).lower().__contains__(str(self.sub_category).lower()),
                        "Title not contains category name")
        DeviceCategory.clear_and_set_sorting_price(self, self.driver,
                                                   self.price_input_type, self.price_value)
        DeviceCategory.click_ok_button(self, self.driver)
        self.assertTrue(DeviceCategory.check_is_all_goods_prices_less_than_choosen(self, self.driver, self.price_value),
                        "One or more things have price more than choosen")
        DeviceCategory.click_check_box_filter(self, self.driver, self.brand_name)
        self.assertTrue(DeviceCategory.verify_is_search_think_present_in_goods_title(self, self.driver, self.brand_name)
                        , "Search result don`t contains chosen brand")
        DeviceCategory.click_check_box_filter(self, self.driver, self.is_available)
        length = DeviceCategory.check_is_all_goods_available(self, self.driver,
                                                             self.not_available)
        self.assertEqual(length, 0, "One or more goods are not available")

    def testVerifySortByPrice(self):
        self.main_part()
        DeviceCategory.clickDropdownOption(self, self.driver, self.cheap)
        is_good_prices_low_to_hight = DeviceCategory.isAllGoodsSortedFromLowToHighPrice(self, self.driver)
        self.assertTrue(is_good_prices_low_to_hight, "One or more prices not sorted from low to high price")
        DeviceCategory.clickDropdownOption(self, self.driver, self.expensive)
        is_good_prices_hight_to_low = DeviceCategory.isAllGoodsSortedFromHighToLowPrice(self, self.driver)
        self.assertTrue(is_good_prices_hight_to_low, "One or more prices not sorted from high to low price")

    def testVerifyItemRamAndPrice(self):
        self.main_part()
        DeviceCategory.choose_ram_сapacity(self, self.driver, self.ram_capacity)
        DeviceCategory.click_check_box_filter(self, self.driver, self.color)
        smartphone_price = DeviceCategory.getSmartphonePriceText(self, self.driver, self.index)
        DeviceCategory.clickLinkMoreAboutDevice(self, self.driver, self.index)
        short_characteristics = DevicePage.verify_device_short_characteristic(self, self.driver, self.ram_capacity)
        chosen_device_price = DevicePage.get_chosen_product_price(self, self.driver)
        self.assertTrue(short_characteristics, "Short_characteristics don't contains chosen ram capacity")
        self.assertEqual(smartphone_price, chosen_device_price, "Prices are not equals")

    def testVerifyAddingAndCountGoodsInBasket(self):
        self.main_part()
        self.assertFalse(DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, self.driver),
                         "Cart Goods Counter Text isn't presented")
        DeviceCategory.clickBuyButtonByIndex(self, self.driver, self.index)
        self.assertTrue(DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, self.driver),
                        "Cart Goods Counter Text isn't presented")

    def testVerifyUsualPriceItemAndInBasket(self):
        self.main_part()
        smartphone_price = DeviceCategory.getSmartphonePriceText(self, self.driver, self.index)
        short_characteristics = DeviceCategory.get_goods_title_text_by_index(self, self.driver, self.index)
        DeviceCategory.clickBuyButtonByIndex(self, self.driver, self.index)
        DeviceCategory.clickOnShoppingBasketButton(self, self.driver)
        item_card_description_text = ShoppingBasket.get_goods_description_text_by_index(self, self.driver, self.index)
        self.assertEqual(short_characteristics, item_card_description_text, "Device Short_characteristics not equals")
        shopping_basket_item_price = ShoppingBasket.getDevicePriceText(self, self.driver, self.index)
        self.assertEqual(smartphone_price, shopping_basket_item_price, "Prices are not equals")
        ShoppingBasket.set_goods_count_value(self, self.driver, self.count)
        # changed_item_price = ShoppingBasket.getSumPriceText(self, self.driver)
        # self.assertEqual(changed_item_price, (smartphone_price * self.count), "Prices are not equals")
        # ----------------------------------------work
        smartphone_price_multiply = (smartphone_price * self.count)
        time.sleep(2)
        self.assertEqual(smartphone_price_multiply, ShoppingBasket.getSumPriceText(self, self.driver),
                         "Prices are not equals")

    def testAddGoodsInBasketAndCheckItEmpty(self):
        self.main_part()
        DeviceCategory.clickBuyButtonByIndex(self, self.driver, self.index)
        DeviceCategory.clickOnShoppingBasketButton(self, self.driver)
        self.assertFalse(ShoppingBasket.isBasketEmptyStatusTextPresent(self, self.driver),
                         "Basket empty status text is presented")
        goods_in_shopping_basket_count = ShoppingBasket.getGoodsInCartListSize(self, self.driver)
        self.assertTrue(goods_in_shopping_basket_count > 0, "Basket is empty")

    def testVerifyItemRamMatrixTypeAndProcessor(self):
        driver = self.driver
        driver.get("https://rozetka.com.ua/ua/")
        driver.maximize_window()
        laptop_category = "Ноутбуки"
        laptop_sub_category = "моноблоки"
        processor_name = "Intel Core i5"
        pc_type = "Моноблок"
        ram = "8 ГБ"
        matrix_type = "IPS"
        MainPage.click_universal_category_link(self, laptop_category, driver)
        SubCategory.click_universal_subcategory_menu_link(self, laptop_sub_category, driver)
        DeviceCategory.click_check_box_filter(self, driver, processor_name)
        DeviceCategory.click_check_box_filter(self, driver, pc_type)
        DeviceCategory.click_check_box_filter(self, driver, ram)
        DeviceCategory.clickUniversalShowCheckBoxButton(self, driver, "Тип матриці")
        DeviceCategory.click_check_box_filter(self, driver, matrix_type)
        DeviceCategory.click_check_box_filter(self, driver, "Новий")
        DeviceCategory.click_check_box_filter(self, driver, "Є в наявності")
        length = DeviceCategory.check_is_all_goods_available(self, driver,
                                                             "Немає в наявності")
        self.assertEqual(length, 0, "One or more goods are not available")
        DeviceCategory.clickLinkMoreAboutDevice(self, driver, 1)
        self.assertTrue(DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, processor_name),
                        "Processor name text not contains in about device text")
        self.assertTrue(DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, ram),
                        "Ram text not contains in about device text")
        self.assertTrue(DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, matrix_type),
                        "Matrix type text not contains in about device text")
        self.assertTrue(DevicePage.verifyChosenParamInAllCharacteristics(self, driver, pc_type),
                        "Computer type text not contains in description device text")

    def test_verify_correct_main_search(self):
        driver = self.driver
        driver.get("https://rozetka.com.ua/ua/")
        driver.maximize_window()
        search_text = "Agm A9"
        MainPage.set_search_input(self, driver, search_text)
        MainPage.click_search_button(self, driver)
        assert MainPage.verify_is_search_brand_present_in_goods_title(self, driver, search_text)

    def test_verify_uncorrect_main_search(self):
        driver = self.driver
        driver.get("https://rozetka.com.ua/ua/")
        driver.maximize_window()
        search_text = "hgvhvg"
        MainPage.set_search_input(self, driver, search_text)
        MainPage.click_search_button(self, driver)
        self.assertTrue(MainPage.verify_wrong_search_request(self, driver), "Wrong request text isn`t presented")

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
