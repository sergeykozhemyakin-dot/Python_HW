from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_delay(self) :
        input_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys("45")

    def buttons_of_calc(self):
        buttons = ["7", "+", "8", "="]
        for btn in buttons:
            self.driver.find_element(By.XPATH, f'//span[text()="{btn}"]').click()

    def get_result(self):
        wait = WebDriverWait(self.driver, 46)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result_text

    def quit(self):
        self.driver.quit()












