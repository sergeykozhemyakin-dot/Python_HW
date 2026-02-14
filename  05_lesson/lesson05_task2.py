from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")
button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
button.click()

sleep(5)

driver.quit()