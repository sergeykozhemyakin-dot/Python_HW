from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
search_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_field.send_keys("Sky")
sleep(2)
search_field.clear()
sleep(2)
search_field.send_keys("Pro")
sleep(2)

driver.quit()
