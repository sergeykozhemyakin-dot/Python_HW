import pytest
from string_utils import StringUtils

string_utils = StringUtils()



@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    # Негативные проверки
    ("Home", "home"), ("SUn", "sun"),])

def test_capitalize_positive_and_negative  (input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("home", "home"),
    (" home", "home"),
    ("    home", "home"),
     # Негативные проверки
    ("My name", "My name"),
    ("   ",""),
    ("home   ", "home   ")])
def test_trim_positive_and_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("string, symbol , expected", [
    ("Home", "o", True),
    ("Hello", "y", False),
    ("Тест", "с", True),
    ("учёба", "ё", True ),
    ("Тортик", "ю", False)
                            ])
def test_contains_positive_and_negative(string, symbol, expected):
    result = string_utils.contains(string, symbol)
    assert result == expected, f"string='{string}', symbol='{symbol}': expected {expected}, got {result}"


@pytest.mark.parametrize("string, symbol, expected", [
    ("Home", "H", "ome"),
    ("Hello world", "о", "Hell wrld"),
    ("banana", "na", "ba"),
    #Негативные проверки
    ("Hello", "world","Hello"),
    ("Home", "i","Home" ),
    ("world", "World", "world")])

def test_delete_symbol(string, symbol, expected):
    result = string_utils.delete_symbol(string, symbol)



