from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://uitestingplayground.com/textinput")
search_field = driver.find_element(By.ID, "newButtonName")
search_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")
button.click()

new_button = driver.find_element(By.ID, "updatingButton")
print(new_button.text)
driver.quit()

