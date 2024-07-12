import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Basepage
from pages.pha import Pharma

@pytest.mark.usefixtures('setup')
class Test_new:

    def test_01_search_and_comparing_after_product_adding_to_cart(self):
        self.base_page = Basepage(self.driver)
        self.pharma = Pharma(self.driver)
        self.pharma.searching_product_name("Ecosprin 75mg Strip Of 14 Tablets")
        self.pharma.all_products_list_click_product()
        self.pharma.click_add_to_cart_btn()
        self.pharma.click_o_carts()
        self.pharma.comparing_the_price()
        assert self.pharma.cart_price == self.pharma.price, "Price is not match"


    def test_02_check_the_title(self):
        self.base_page = Basepage(self.driver)
        self.pharma = Pharma(self.driver)
        assert self.base_page.get_title() == "PharmEasy: Online Pharmacy & Medical Store in India | 50 Lakhs+ Customers."

    def test_03_check_the_logo_is_display(self):
        self.base_page = Basepage(self.driver)
        self.pharma = Pharma(self.driver)
        assert self.base_page.is_display(self.pharma.CHECK_LOGO_IS_VISIBLE) == True

    def test_04_user_can_delete_the_product_from_cart(self):
        self.base_page = Basepage(self.driver)
        self.pharma = Pharma(self.driver)
        self.pharma.searching_product_name("Ecosprin 75mg Strip Of 14 Tablets")
        self.pharma.all_products_list_click_product()
        self.pharma.click_add_to_cart_btn()
        self.pharma.click_o_carts()
        self.pharma.remove_the_product_form_cart()
        assert (self.base_page.get_text(self.pharma.CHECK_AFTER_REMOVING_PRODUCT_TEXT_CSS)
                == "0 Items in your Cart"), ("Product still is on your cart", self.base_page.take_screenshot("removed"))









