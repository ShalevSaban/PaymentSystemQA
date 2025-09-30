# payment_credit_card_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PaymentOptionsPage:

    def __init__(self, driver):
        """Wait for payment page to load"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located((By.ID, "Gr0W8-payment-btns")))
        print("Options loaded")

    def click_credit_card_payment(self):
        """Click credit card payment button"""
        try:
            credit_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "Gr0W8-btn-credit"))
            )
            credit_btn.click()
            print("Clicked Credit Card Payment")
            time.sleep(3)
        except Exception as e:
            print(f"Error clicking credit card button: {e}")


