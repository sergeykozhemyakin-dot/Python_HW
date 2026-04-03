import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from login_page import LoginPage
from main_page import MainPage
from order import Order


@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("Магазин")
@allure.story("Покупка товара")
@allure.title("Весь цикл оформления заказа")
@allure.description(
    "Тест проверяет авторизацию, ввод данных пользователя и итоговую сумму заказа"
)
def test_store(firefox_driver: WebDriver) -> None:
    login_page = LoginPage(firefox_driver)
    login_page.login("standard_user", "secret_sauce")
    main_page = MainPage(firefox_driver)
    main_page.add_to_cart()
    order = Order(firefox_driver)
    order.user_profile("Сергей", "Кожемякин", "236029")
    order.result()
