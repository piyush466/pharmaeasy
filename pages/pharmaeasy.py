import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Pharma:

    # Locators for various elements on the page
    SEARCH_BAR_BY_XPATH = "(//span[text()='Search for'])[2]"
    SEARCH_PRODUCT_NAME_BY_ID = "topBarInput"
    CLICK_ON_ADD_TO_CART_BTN_By_XPATH = "//button[text()='Add To Cart']"
    SELECT_MAX_VALUE_BY_CSS = "li[data-value='20']"
    CLICK_ON_CART_BY_CSS = 'a[href="/cart?src=header"]'
    REMOVE_THE_PRODUCTS_BY_CLASS = "styles_removeItemButton__oEO4y"
    REMOVE_CLICK_BY_CSS = "[class='ClickableElement_clickable__ItKj2 style_button__rZqYO']"

    def __init__(self, driver):
        # Initialize the Pharma class with the WebDriver instance and WebDriverWait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_product_name(self, product_name):
        # Click on the search bar, enter the product name, and press Enter
        self.ele = self.driver.find_element(By.XPATH, self.SEARCH_BAR_BY_XPATH)
        self.driver.execute_script("arguments[0].click();", self.ele)
        self.name = self.driver.find_element(By.ID, self.SEARCH_PRODUCT_NAME_BY_ID)
        self.name.send_keys(product_name)
        self.name.send_keys(Keys.ENTER)

    def click_on_add_to_cart_button(self):
        # Wait until the 'Add To Cart' button is clickable and then click it
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.CLICK_ON_ADD_TO_CART_BTN_By_XPATH))).click()

    def select_max_value(self):
        # Scroll down and select the maximum value from the dropdown
        self.driver.execute_script("window.scrollBy(0,1140)")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.SELECT_MAX_VALUE_BY_CSS))).click()

    def click_on_cart(self):
        # Wait until the cart icon is clickable and then click it
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.CLICK_ON_CART_BY_CSS))).click()

    def remove_the_price(self):
        # Click on the remove button and confirm removal of the product
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.REMOVE_THE_PRODUCTS_BY_CLASS))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.REMOVE_CLICK_BY_CSS))).click()
