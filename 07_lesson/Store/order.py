from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Order:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def user_profile(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Сергей")
        self.driver.find_element(By.ID, "last-name").send_keys("Кожемякин")
        self.driver.find_element(By.ID, "postal-code").send_keys("236029")
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