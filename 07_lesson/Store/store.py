from login_page import LoginPage
from main_page import MainPage
from order import Order

def test_store(firefox_driver):
    login_page = LoginPage(firefox_driver)
    login_page.login("standard_user", "secret_sauce" )
    main_page = MainPage(firefox_driver)
    main_page.add_to_cart()
    order = Order(firefox_driver)
    order.user_profile("Сергей", "Кожемякин", "236029")
    order.result()

