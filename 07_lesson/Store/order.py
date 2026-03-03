from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Order:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def user_profile(self, first_name, last_name, postal_code):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        last_name_field = self.wait.until(EC.presence_of_element_located((By.ID,"last-name")))
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        postal_code_field = self.wait.until(EC.presence_of_element_located((By.ID, "postal-code")))
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        return

    def result(self):
        total_price = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))).text
        price ="$58.29"
        assert price in total_price
        print(" РЕЗУЛЬТАТ ТЕСТА")
        print(f" {total_price}")
        print(f" Ожидалось: {price}")
        self.driver.find_element(By.ID, "finish").click()
        return self