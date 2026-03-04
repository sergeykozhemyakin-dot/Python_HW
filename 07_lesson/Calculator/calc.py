import pytest
from calculator_page import CalculatorPage

def test_calculator(chrome_driver):
    calc = CalculatorPage(chrome_driver)
    calc.input_delay()
    calc.buttons_of_calc()
    result = calc.get_result()
    print(f'Результат: {result}')
    assert result == "15", f"Ожидалось 15, получено {result}"




