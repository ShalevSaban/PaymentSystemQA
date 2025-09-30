from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from config import PRODUCTS, MAX_ITEMS_IN_CART, PAYMENT_URL,OPT,TEST_CARD
from pages.products_page import ProductsPage
from pages.details_page import DetailsPage
from pages.payment_credit_page import PaymentCreditCardPage
from pages.payments_options_page import PaymentOptionsPage

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
driver.get(PAYMENT_URL)

productsPage=ProductsPage(driver)

productsPage.add_item(PRODUCTS["SHAKSHUKA"]["index"],3)
productsPage.click_continue()

detailsPage=DetailsPage(driver)

detailsPage.fill_form(
    full_name="ישראל ישראלי",
    phone="0501234567",
    preparation_index=OPT["preparation"]["immediately"],
    pickles_index=OPT["pickles"]["yes"],
    chips_index=OPT["chips"]["no"],
    shipping_index=OPT["shipping"]["pickup"],
    address="תל אביב",
    notes="abc",  # Max 3 characters
    source_index=OPT["source"]["instagram"])

detailsPage.accept_terms()
detailsPage.click_continue()

paymentOptionsPage=PaymentOptionsPage(driver)
paymentOptionsPage.click_credit_card_payment()

paymentCreditPage=PaymentCreditCardPage(driver)

paymentCreditPage.fill_credit_card(
    card_number=TEST_CARD["number"],
    exp_month=TEST_CARD["exp_month"],
    exp_year=TEST_CARD["exp_year"],
    cvv=TEST_CARD["cvv"],
    personal_id="322358466"
)

paymentCreditPage.submit_payment()
paymentCreditPage.click_finish()




time.sleep(5)  # So you can see the result
driver.quit()