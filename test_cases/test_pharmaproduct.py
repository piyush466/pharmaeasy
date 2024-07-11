import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.pharmaeasy import Pharma


class Test_pharma:
    product_name="Ecosprin 75mg Strip Of 14 Tablets"
    ALL_PRODUCTS_NAME = By.CSS_SELECTOR, "h1"
    CLICK_ON_ADD_TO_CART_BTN = By.CSS_SELECTOR, "button"
    PRICE_OF_PRODUCT_BY_CSS = '[class="style_bold__edLw2"]'
    CART_TOTAL_PRICE_BY_CSS = "[class='AmountBifurcation_finalValue__MkWUw AmountBifurcation_finalValueBold__r8tdR']"



    def test_pharma_product_price(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver,10)
        self.pharma = Pharma(self.driver)
        self.pharma.search_product_name(self.product_name)
        self.products = self.wait.until(EC.visibility_of_all_elements_located(self.ALL_PRODUCTS_NAME))

        for self.product in self.products:
            if self.product.text == "Ecosprin 75mg Strip Of 14 Tablets":
                self.product.click()
                break
        self.pharma.click_on_add_to_cart_button()
        self.pharma.select_max_value()
        self.pharma.click_on_cart()
        self.price = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRICE_OF_PRODUCT_BY_CSS))).text
        print(self.price)
        self.products_price = self.price.replace("₹", "")
        self.convert_product_price  = float(self.products_price)
        self.cart_price = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CART_TOTAL_PRICE_BY_CSS))).text
        print(self.cart_price)
        assert self.price == self.cart_price
        self.pharma.remove_the_price()


    def test_02_title_match(self,setup):
        self.driver = setup
        self.expected_title = self.driver.title
        if self.expected_title == "PharmEasy: Online Pharmacy & Medical Store in India | 50 Lakhs+ Customers.":
            assert True
        else:
            self.driver.save_screenshot("../screenshot/test_02.png")
            assert False






