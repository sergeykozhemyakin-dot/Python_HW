import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Оформление заказа")
class Order:
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.story("Оформление профиля")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Ввод данных пользователя")
    def user_profile(
        self, first_name: str, last_name: str, postal_code: str
    ) -> "Order":
        """
        Заполняет данные покупателя: имя, фамилию и почтовый индекс.
        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        :return: Экземпляр текущего класса Order.
        """
        with allure.step(f"Ввод имени {first_name}"):
            first_name_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )
            first_name_field.clear()
            first_name_field.send_keys(first_name)
        with allure.step(f"Ввод фамилии {last_name}"):
            last_name_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "last-name"))
            )
            last_name_field.clear()
            last_name_field.send_keys(last_name)
        with allure.step(f"Ввод почтового индекса {postal_code}"):
            postal_code_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "postal-code"))
            )
            postal_code_field.clear()
            postal_code_field.send_keys(postal_code)
        with allure.step("Переход к следующему этапу"):
            self.driver.find_element(By.ID, "continue").click()
        return

    @allure.story("Итоговая проверка")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка итоговой стоимости")
    @allure.description("Сравнение фактической сумы покупки в корзине с ожидаемой")
    def result(self) -> None:
        """
        Проверяет итоговую сумму и завершает оформление заказа.
        :return: None
        """
        with allure.step("Итоговая сумма"):
            total_price = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".summary_total_label")
                )
            ).text
            price = "$58.29"
        with allure.step("Сравнение итоговой суммы и заданной"):
            assert price in total_price
            print(" РЕЗУЛЬТАТ ТЕСТА")
            print(f" {total_price}")
            print(f" Ожидалось: {price}")
            self.driver.find_element(By.ID, "finish").click()
            return self
