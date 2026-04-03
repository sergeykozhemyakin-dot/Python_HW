import allure
from calculator_page import CalculatorPage


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Математические операции")
@allure.story("Сложение с задержкой")
@allure.title("Проверка действия 7 + 8 с ожиданием ")
@allure.description("Тест устанавливает задержку выполнения в  45 сек ")
def test_calculator(chrome_driver):
    calc = CalculatorPage(chrome_driver)
    calc.input_delay()
    calc.buttons_of_calc()
    result = calc.get_result()
    print(f"Результат: {result}")
    assert result == "15", f"Ожидалось 15, получено {result}"
