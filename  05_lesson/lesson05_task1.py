from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()


driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

sleep(5)

driver.quit()