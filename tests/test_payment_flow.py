import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.products_page import ProductsPage
from pages.details_page import DetailsPage
from pages.payments_options_page import PaymentOptionsPage
from pages.payment_credit_page import PaymentCreditCardPage
from config import PRODUCTS, OPT


class TestHappyPath:

    def test_basic_purchase(self, driver, basic_customer,test_card):

        products_page = ProductsPage(driver)
        products_page.add_item(PRODUCTS["HUMMUS"]["index"], 1)
        products_page.click_continue()

        details_page = DetailsPage(driver)
        details_page.fill_form(**basic_customer)
        details_page.accept_terms()
        details_page.click_continue()

        paymentOptionsPage=PaymentOptionsPage(driver)
        paymentOptionsPage.click_credit_card_payment()

        paymentCreditPage=PaymentCreditCardPage(driver)
        paymentCreditPage.fill_credit_card(**test_card)
        paymentCreditPage.submit_payment()
        paymentCreditPage.click_confirm_button()

        paymentCreditPage.verify_redirect_to_confirmation() # assert operation

class TestValidationPath:

    def test_empty_fullname_validation(self, driver, basic_customer):
        """Test empty fullname field shows error"""
        products_page = ProductsPage(driver)
        products_page.add_item(PRODUCTS["HUMMUS"]["index"], 1)
        products_page.click_continue()

        details_page = DetailsPage(driver)

        # Fill form without fullname
        customer = basic_customer.copy()
        customer['full_name'] = ''

        details_page.fill_form(**customer)
        details_page.accept_terms()
        details_page.click_continue()

        # Verify error displayed
        assert details_page.verify_input_error("fullName")


    def test_empty_phone_validation(self, driver, basic_customer):
        """Test empty phone field shows error"""
        products_page = ProductsPage(driver)
        products_page.add_item(PRODUCTS["HUMMUS"]["index"], 1)
        products_page.click_continue()

        details_page = DetailsPage(driver)

        # Fill form without phone
        customer = basic_customer.copy()
        customer['phone'] = ''

        details_page.fill_form(**customer)
        details_page.accept_terms()
        details_page.click_continue()

        # Verify error displayed
        assert details_page.verify_input_error("phone")

    def test_invalid_credit_card(self, driver, basic_customer, test_card):
        """Test invalid credit card shows error"""
        # Navigate to payment page
        products_page = ProductsPage(driver)
        products_page.add_item(PRODUCTS["HUMMUS"]["index"], 1)
        products_page.click_continue()

        details_page = DetailsPage(driver)
        details_page.fill_form(**basic_customer)
        details_page.accept_terms()
        details_page.click_continue()

        payment_options_page = PaymentOptionsPage(driver)
        payment_options_page.click_credit_card_payment()

        # Fill invalid card and verify error
        payment_credit_page = PaymentCreditCardPage(driver)
        invalid_card = test_card.copy()
        invalid_card["card_number"] = "1234567890123456"

        payment_credit_page.fill_credit_card(**invalid_card)
        payment_credit_page.submit_payment()

        assert payment_credit_page.verify_credit_card_error("card_number")
