import time
import allure
from pages.main_page import MainPage
import pytest
import logging
from pytest_zebrunner import attach_test_artifact
import pyscreenrec
from utils.attachments import attach_screenshot, attach_logs, attach_recorded_video

@allure.suite('MainPage')
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
        attach_test_artifact("../recording.mp4")
        attach_screenshot()
        attach_logs(logging.INFO, 'Test was successful')
        assert main_page.verify_is_search_brand_present_in_goods_title(search_text), "Search text not" \
                                                                                     " contains in all " \
                                                                                     "goods title texts"

    @pytest.mark.label("Search", "Incorrect")
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
