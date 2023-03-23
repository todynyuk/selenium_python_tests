import time
import allure
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.sub_category_page import SubCategory
import logging
import pyscreenrec
from utils.attachments import attach_screenshot, attach_logs, attach_recorded_video
import os


@allure.suite('DevicePage')
class TestDetailsPage:
    @allure.title('Check verify in chosen device ram and price')
    def testItemRamAndPrice(self, driver):
        os.remove("recording.mp4")
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
        attach_screenshot()
        chosen_device_price = DevicePage.get_chosen_product_price(self, driver)
        assert short_characteristics, "Short_characteristics don't contains chosen ram capacity"
        assert str(smartphone_price) == chosen_device_price, "Prices are not equals"
        attach_logs(logging.INFO, 'Test was successful')
