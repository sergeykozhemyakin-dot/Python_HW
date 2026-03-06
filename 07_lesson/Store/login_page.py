from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(driver, 10)

    def login(self, user_name, password):
        login_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        login_field.clear()
        login_field.send_keys(user_name)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

        self.driver.find_element(By.ID, "login-button").click()
