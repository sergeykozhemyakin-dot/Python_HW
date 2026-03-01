from selenium import webdriver
from calculator_page import CalculatorPage

def test_calculator():
    driver =webdriver.Chrome()
    calc = CalculatorPage(driver)
    calc.input_delay()
    calc.buttons_of_calc()
    result = calc.get_result()
    print(f'Результат: {result}')
    assert result == "15", f"Ожидалось 15, получено {result}"

    calc.quit()




