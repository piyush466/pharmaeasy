import time
import pytest
from pages.base_page import Basepage
from pages.pharmaeasy_page import Pharma


@pytest.mark.usefixtures('setup')
class Test_new:

    def test_01_search_and_comparing_after_product_adding_to_cart(self):
        # Initialize page objects
        self.base_page = Basepage(self.driver)
        self.pharma = Pharma(self.driver)

        # Search for a product and add it to the cart
        self.pharma.searching_product_name("Ecosprin 75mg Strip Of 14 Tablets")
        self.pharma.all_products_list_click_product()
        self.pharma.click_add_to_cart_btn()
        self.pharma.click_o_carts()

        # Compare the product price in the cart with the product price
        self.pharma.comparing_the_price()
        assert self.pharma.cart_price == self.pharma.price, "Price does not match"

    def test_02_check_the_title(self):
        # Initialize page objects
        self.base_page = Basepage(self.driver)

        # Verify the title of the page
        assert self.base_page.get_title() == "PharmEasy: Online Pharmacy & Medical Store in India | 50 Lakhs+ Customers."

    def test_03_check_the_logo_is_display(self):
        # Initialize page objects
        self.base_page = Basepage(self.driver)
        self.pharma = Pharma(self.driver)

        # Check if the logo is displayed on the page
        assert self.base_page.is_display(self.pharma.CHECK_LOGO_IS_VISIBLE) == True

    def test_04_user_can_delete_the_product_from_cart(self):
        # Initialize page objects
        self.base_page = Basepage(self.driver)
        self.pharma = Pharma(self.driver)

        # Search for a product, add it to the cart, and then remove it
        self.pharma.searching_product_name("Ecosprin 75mg Strip Of 14 Tablets")
        self.pharma.all_products_list_click_product()
        self.pharma.click_add_to_cart_btn()
        self.pharma.click_o_carts()
        self.pharma.remove_the_product_form_cart()

        # Verify that the product is removed from the cart
        assert (self.base_page.get_text(self.pharma.CHECK_AFTER_REMOVING_PRODUCT_TEXT_CSS)
                == "0 Items in your Cart"), ("Product is still in your cart", self.base_page.take_screenshot("removed1"))
