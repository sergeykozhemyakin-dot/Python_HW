import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class CalculatorPage:
    """
    Класс для работы со страницей медленного калькулятора.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.driver.get(url=
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установка задержки таймера на 45 секунд")
    def input_delay(self) -> None:
        """
        Устанавливает значение задержки в поле ввода.
        :return: None
        """
        input_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys("45")

    @allure.step("Нажатие клавиш 7, +, 8, и  = на калькуляторе ")
    def buttons_of_calc(self) -> None:
        """
        Последовательно нажимает кнопки на панели калькулятора.
        :return: None
        """
        buttons = ["7", "+", "8", "="]
        for btn in buttons:
            self.driver.find_element(By.XPATH, f'//span[text()="{btn}"]').click()

    @allure.step("Вывод результата вычисления ")
    def get_result(self) -> str:
        """
        Ожидает появления результата и возвращает текст с экрана калькулятора.
        :return: Строковое значение результата (например, "15").
        """
        wait = WebDriverWait(self.driver, 46)
        wait.until(es.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result_text
