import logging

import pytest
from pytest_zebrunner import *
from pytest_zebrunner import CurrentTestRun
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunPyTest", "PyTest")
attach_test_run_label("TestRunPyTestNew", "Zebrunner")

attach_test_run_artifact_reference("Zebrunner", "https://zebrunner.com/")
attach_test_run_artifact_reference("PyTest", "https://docs.pytest.org/en/latest/")
attach_test_run_artifact_reference("PyTest Zebrunner agent", "https://zebrunner.com/documentation/reporting/pytest/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")

# Test data
url = "https://www.google.com/"
cookies_dialog_test = "Before you continue to Google Search"
search_value = "Zebrunner"


def test_advanced(driver):
    logger.info("'test_advanced' test was started")

    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Zebrunner")
    attach_test_artifact_reference("TestArtifactReference", "https://zebrunner.com/")

    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)

    if driver.page_source.find(cookies_dialog_test) != -1:
        logger.info("Cookies use popup is displayed, necessary to click 'Accept all'")
        driver.find_element(by=By.XPATH, value="//button[.='Accept all']").click()
        attach_screenshot(driver)

    logger.info("Performing search with value: " + search_value)
    search_field: WebElement = driver.find_element(by=By.XPATH, value="//input[@name='q']")
    search_field.send_keys(search_value)
    search_field.send_keys(Keys.ENTER)
    attach_screenshot(driver)

    logger.info("Verify first search result contains: '" + search_value + "'")
    first_link: WebElement = driver.find_element(by=By.XPATH, value="//*[@id='search']//a")
    logger.info(first_link.text)
    assert first_link.text.find(search_value) != -1
    logger.info("'test_advanced' test was finished")


def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")
