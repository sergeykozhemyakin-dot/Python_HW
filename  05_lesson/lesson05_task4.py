from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
sleep(2)
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit")
login_button.click()
sleep(2)
driver.quit()