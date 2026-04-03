import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    """
    Класс для работы с главной страницей магазина (каталогом).
    """

    def __init__(self, driver):
        """
        Инициализация главной страницы.
        :param driver: Экземпляр WebDriver (Chrome/Firefox).
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self) -> None:
        """
        Находит товары на странице и добавляет их в корзину.
        :return: None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
