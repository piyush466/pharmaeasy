import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Basepage

class Pharma(Basepage):

    # Locators for various elements on the page
    SEARCH_BAR_BY_XPATH = "(//span[text()='Search for'])[2]"
    SEARCH_PRODUCT_NAME_BY_ID = (By.ID, "topBarInput")
    CLICK_ON_ADD_TO_CART_BTN_By_XPATH = (By.XPATH, "//button[text()='Add To Cart']")
    SELECT_MAX_VALUE_BY_CSS = (By.CSS_SELECTOR, "li[data-value='20']")
    CLICK_ON_CART_BY_CSS = (By.CSS_SELECTOR, 'a[href="/cart?src=header"]')
    REMOVE_THE_PRODUCTS_BY_CLASS = (By.CLASS_NAME, "styles_removeItemButton__oEO4y")
    REMOVE_CLICK_BY_CSS = (By.CSS_SELECTOR, "[class='ClickableElement_clickable__ItKj2 style_button__rZqYO']")
    ALL_PRODUCTS_NAME = (By.CSS_SELECTOR, "h1")
    PRICE_OF_PRODUCT_BY_CSS = (By.CSS_SELECTOR, '[class="style_bold__edLw2"]')
    CART_TOTAL_PRICE_BY_CSS = (By.CSS_SELECTOR, "[class='AmountBifurcation_finalValue__MkWUw AmountBifurcation_finalValueBold__r8tdR']")
    CHECK_LOGO_IS_VISIBLE = (By.CSS_SELECTOR, "[class='c-PJLV c-bXbWpx c-bXbWpx-igFlfzW-css']")
    CHECK_AFTER_REMOVING_PRODUCT_TEXT_CSS = (By.CSS_SELECTOR, "[class='styles_cartCount__uDXZh'] span")

    def searching_product_name(self, product_name):
        # Click on the search bar and enter the product name, then press Enter
        self.ele = self.driver.find_element(By.XPATH, self.SEARCH_BAR_BY_XPATH)
        self.driver.execute_script("arguments[0].click();", self.ele)
        self.send_keys(self.SEARCH_PRODUCT_NAME_BY_ID, product_name)
        self.send_keys(self.SEARCH_PRODUCT_NAME_BY_ID, Keys.ENTER)

    def click_add_to_cart_btn(self):
        # Click the 'Add To Cart' button and select the maximum value from the dropdown
        self.do_click(self.CLICK_ON_ADD_TO_CART_BTN_By_XPATH)
        self.scroll_down(0, 1140)
        self.do_click(self.SELECT_MAX_VALUE_BY_CSS)

    def click_o_carts(self):
        # Click on the cart icon and wait for 2 seconds
        self.do_click(self.CLICK_ON_CART_BY_CSS)
        time.sleep(2)

    def remove_the_product_form_cart(self):
        # Remove the product from the cart and wait for 3 seconds
        self.do_click(self.REMOVE_THE_PRODUCTS_BY_CLASS)
        self.do_click(self.REMOVE_CLICK_BY_CSS)


    def all_products_list_click_product(self):
        # Wait until all product names are visible, then click on the specified product and refresh the page
        self.all_poducts = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.ALL_PRODUCTS_NAME))
        for self.products in self.all_poducts:
            print(self.products.text)
            if self.products.text == "Ecosprin 75mg Strip Of 14 Tablets":
                self.products.click()
                self.driver.refresh()
                break

    def comparing_the_price(self):
        # Compare the price of the product with the cart total price
        self.price = self.get_text(self.PRICE_OF_PRODUCT_BY_CSS)
        print(self.price)
        self.products_price = self.price.replace("₹", "")
        self.convert_product_price = float(self.products_price)
        self.cart_price = self.get_text(self.CART_TOTAL_PRICE_BY_CSS)
        # print(self.cart_price)

    def after_removing_text(self):
        # Print the text that appears after removing a product from the cart
        print(self.get_text(self.CHECK_AFTER_REMOVING_PRODUCT_TEXT_CSS))
