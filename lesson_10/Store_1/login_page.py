import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Личный кабинет пользователя")
class LoginPage:
    def __init__(self, driver) -> None:
        """
        Инициализация страницы логина.
        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(driver, 10)

    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Вход в систему под пользователем { user_name}")
    def login(self, user_name=str, password=str) -> None:
        """
        Выполняет вход в систему с указанными учетными данными.
        :param user_name: Логин пользователя.
        :param password: Пароль пользователя.
        :return: None
        """
        with allure.step("Ввод логина"):
            login_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            login_field.clear()
            login_field.send_keys(user_name)

            with allure.step("Ввод пароля"):
                password_field = self.driver.find_element(By.ID, "password")
                password_field.clear()
                password_field.send_keys(password)

            with allure.step("Нажатие на кнопку ввод"):
                self.driver.find_element(By.ID, "login-button").click()
