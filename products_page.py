from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductsPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Find all product containers once
        self.product_containers = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div[class*='checkbox_checkbox-content']")
            )
        )
        print(f"Page loaded: {len(self.product_containers)} products found")


    def add_item(self,index,quantity):
        item=self.product_containers[index]
        label =item.find_element(By.CSS_SELECTOR, "label[for*='product_checkbox']")
        product_name = item.find_element(By.TAG_NAME, "h3").text
        print(f"\nProduct: {product_name}")
        print(f"Clicking checkbox...")
        label.click()
        plus_button = item.find_element(By.CSS_SELECTOR, "button[aria-label*='להוספת כמות']")
        for i in range(quantity):
            plus_button.click()
            print(f"Click {i+1} plus button")
        print(f"Item added {quantity} times!")


    def click_continue(self):
        """Click continue button"""
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-label*='המשך']")
            )
        )
        continue_btn.click()
        print("Clicked Continue")
        time.sleep(1)