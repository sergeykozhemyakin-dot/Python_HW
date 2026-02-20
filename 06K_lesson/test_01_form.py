from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_foam():
    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 20)

    fields_to_fill = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields_to_fill.items():
        field = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}'].form-control")
        field.send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert")))

    zip_element = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_element.get_attribute("class"), "Zip-code не красный"
    assert zip_element.text == "N/A", "Текст zip-code не N/A"
    print(" Zip-code красный (верно)")

    for field_id in fields_to_fill.keys():
        element = driver.find_element(By.ID, field_id)
        element_class = element.get_attribute("class")
        assert "alert-success" in element_class, f"Поле {field_id} не зеленое! Класс: {element_class}"
        print(f"{field_id} зеленый")


    driver.quit()