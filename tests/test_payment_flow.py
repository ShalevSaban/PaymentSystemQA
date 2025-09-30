# 1. Standard library imports
import time
import pytest

# 2. Third-party imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 3. Local application imports
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



