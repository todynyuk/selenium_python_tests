from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class*='button_color_green']")
    GOODS_TITLE_TEXTS = (By.XPATH, "//span[@class='goods-tile__title']")
    NOT_FOUND_TEXT = (By.XPATH, "//span[@class='ng-star-inserted']")


class DevicePageLocators:
    SHORT_CHARACTERISTICS_TITLE = (By.XPATH, "//h1[@class='product__title']")
    PRODUCT_PRICE = (By.XPATH, "//p[contains(@class,'product-prices__big')]")
    SHORT_CHARACTERISTIC = (By.XPATH, "//p[@class='product-about__brief ng-star-inserted']")
    ALL_CHARACTERISTIC = (By.XPATH,
                          "//h3[@class='product-tabs__heading']//span[contains(@class,'heading_color_gray')]")


