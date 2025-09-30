from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DetailsPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Wait for form to load
        self.wait.until(
            EC.presence_of_element_located((By.NAME, "fullName"))
        )
        print("Payment details page loaded")


    def fill_form(self, full_name, phone, preparation_index=0,
                  pickles_index=0, chips_index=0, shipping_index=0, address="",notes="",source_index=0):
        """Fill all text input fields"""
        # Full name (required)
        # name_field = self.wait.until(
        #     EC.presence_of_element_located((By.NAME, "fullName"))
        # )
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", name_field)
        # time.sleep(0.5)
        name_field = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "fullName"))
        )
        name_field.clear()
        name_field.send_keys(full_name)

        # Phone (required)
        # phone_field = self.wait.until(
        #     EC.presence_of_element_located((By.NAME, "phone"))
        # )
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
        # time.sleep(0.5)
        phone_field = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "phone"))
        )
        phone_field.clear()
        phone_field.send_keys(phone)

        # Address (optional)
        if address:
            address_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", address_field)
            time.sleep(0.5)
            address_field = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "address"))
            )
            address_field.clear()
            address_field.send_keys(address)

        # Notes (optional)
        if notes:
            notes_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "2936"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", notes_field)
            time.sleep(0.5)
            notes_field = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "2936"))
            )
            notes_field.clear()
            notes_field.send_keys(notes)

        # Preparation time dropdown
        self._select_dropdown("2933", preparation_index)
        print(f"Preparation: option {preparation_index}")

        # Pickles radio
        self._select_radio("2934", pickles_index)
        print(f"Pickles: option {pickles_index}")

        # Chips radio
        self._select_radio("2935", chips_index)
        print(f"Chips: option {chips_index}")

        # Shipping dropdown
        self._select_dropdown("shipping", shipping_index)
        print(f"Shipping: option {shipping_index}")

        # Source dropdown
        self._select_dropdown("2937", source_index)
        print(f"Source: option {source_index}")

        print("Form completed\n")

        time.sleep(2)



    def _select_dropdown(self, id, index):
        self.driver.find_element(By.ID, id).click()
        time.sleep(1)
        self.driver.find_elements(By.CSS_SELECTOR, f"li[name='{id}']")[index].click()
        time.sleep(1)

    def _select_radio(self, name, index):
        radios = self.driver.find_elements(By.CSS_SELECTOR, f"input[name='{name}']")
        radio_id = radios[index].get_attribute("id")
        self.driver.find_element(By.CSS_SELECTOR, f"label[for='{radio_id}']").click()
        time.sleep(0.3)


    def accept_terms(self):
        terms_checkbox = self.driver.find_element(By.CSS_SELECTOR, "label[for='termsCheckbox']")
        terms_checkbox.click()
        print("Accepted terms")
        time.sleep(0.5)

    def click_continue(self):

            btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label*='המשך לשלב הבא']"))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            print("JS click used")

            time.sleep(1)



