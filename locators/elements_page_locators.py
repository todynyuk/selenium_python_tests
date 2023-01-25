from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class*='button_color_green']")
    GOODS_TITLE_TEXTS = (By.XPATH, "//span[@class='goods-tile__title']")
    NOT_FOUND_TEXT = (By.XPATH, "//span[@class='ng-star-inserted']")
