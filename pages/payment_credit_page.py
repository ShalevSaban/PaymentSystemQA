# payment_credit_card_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

class PaymentCreditCardPage:

    def __init__(self, driver):
        """Wait for payment page to load"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located((By.ID, "Gr0W8-credit-card-form")))
        time.sleep(3)
        print("Payment page loaded")



    def fill_credit_card(self, card_number, exp_month, exp_year, cvv, personal_id=""):

        try:
           print("--- Filling credit card details ---")
           iframe = self.wait.until(
               EC.presence_of_element_located((By.TAG_NAME, "iframe"))
           )
           self.driver.switch_to.frame(iframe)
           # Card number
           card_field = self.wait.until(EC.element_to_be_clickable((By.ID, "card-number")))
           card_field.clear()
           card_field.send_keys(card_number)
           print(f"Card number filled")

           # Expiry year dropdown
           year_dropdown = Select(self.driver.find_element(By.ID, "expYear"))
           year_dropdown.select_by_value(exp_year)
           print(f"Year: {exp_year}")

           # Expiry month dropdown
           month_dropdown = Select(self.driver.find_element(By.ID, "expMonth"))
           month_dropdown.select_by_value(exp_month)
           print(f"Month: {exp_month}")

           # CVV
           cvv_field = self.driver.find_element(By.ID, "cvv")
           cvv_field.clear()
           cvv_field.send_keys(cvv)
           print(f"CVV filled")

           #Personal ID (Israeli ID)
           id_field = self.driver.find_element(By.ID, "personal-id")
           id_field.clear()
           id_field.send_keys(personal_id)
           print(f"Personal ID filled")

        #self.driver.switch_to.default_content()

        except TimeoutException:
            print("cant find iframe")
            self.driver.switch_to.default_content()
            raise

        print("Credit card form completed\n")

    def submit_payment(self):
        """Click submit payment button"""
        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "cg-submit-btn"))
        )
        submit_btn.click()
        print("Payment submitted")
        time.sleep(3)

    def click_finish(self):

            btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label*='אישור וחזרה']"))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            print("JS click used")

            time.sleep(1)

    def click_confirm_button(self):
        try:
            # Switch back to default content first
            self.driver.switch_to.default_content()

            # Wait for confirm button and click
            confirm_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "Gr0W8-confirm-btn"))
            )
            confirm_btn.click()
            print("Clicked confirm button")
            time.sleep(2)
        except Exception as e:
            print(f"Error clicking confirm button: {e}")

    def verify_redirect_to_confirmation(self):
        self.wait.until(EC.url_contains("sandbox.grow.link/confirmation"))
        assert "sandbox.grow.link/confirmation" in self.driver.current_url
        print("✓ Redirected to confirmation page")