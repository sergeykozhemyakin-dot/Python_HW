from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def test_swag_labs():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Сергей")
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Кожемякин")
    post_code = driver.find_element(By.ID, "postal-code")
    post_code.send_keys("236029")
    driver.find_element(By.ID, "postal-code")
    driver.find_element(By.ID, "continue").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_price = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    if total_price == "$58.29":
        print(f' Итоговая сумма :{total_price}')
    else:
        print("Неверная сумма")


    driver.quit()





