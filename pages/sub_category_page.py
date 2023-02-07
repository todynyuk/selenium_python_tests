from selenium.webdriver.common.by import By
import time


class SubCategory():

    def __init__(self, web_driver, url=''):
        url = 'https://rozetka.com.ua/ua/'
        super().__init__(web_driver, url)

    def click_universal_subcategory_menu_link(self, sub_category, driver):
        driver.find_element(By.XPATH,
                            f"//a[contains(@class,'tile-cats__heading') and contains(.,'{sub_category}')]").click()
        time.sleep(3)
