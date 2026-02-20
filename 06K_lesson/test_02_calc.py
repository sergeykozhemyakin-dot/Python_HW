
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def test_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    input_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    input_field.clear()
    input_field.send_keys("45")
    driver.find_element(By.CSS_SELECTOR, "div.keys > span:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR,  "div.keys > span:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, " div.keys > span:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, " div.keys > span.btn.btn-outline-warning").click()
    waite = WebDriverWait(driver, 46)
    waite.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"
    print(f'Результат:{result}')
    driver.quit()




