from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(16)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.ID, "ajaxButton").click()
green = driver.find_element(By.CSS_SELECTOR, ".bg-success").text
print(green)
driver.quit()