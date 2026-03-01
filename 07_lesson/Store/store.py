from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from order import Order

def test_store():
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.user_personal_data()
    main_page = MainPage(driver)
    main_page.add_to_cart()
    # order = Order(driver)
    # order.user_profile()
    # order.result()
    # driver.quit()

