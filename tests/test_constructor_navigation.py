from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators


class TestConstructorNavigation:

    def test_navigate_to_fillings(self, driver):
        # Нажатие на кнопку "Начинки"
        driver.find_element(By.XPATH, locators.fillings_button).click()
        # Ожидание появления заголовка "Начинки"
        header = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, locators.fillings_header))
        )
        # Проверка видимости заголовка
        assert header.is_displayed(), "Header 'Начинки' is not displayed."

    def test_navigate_to_souces(self, driver):
        # Нажатие на кнопку "Соусы"
        driver.find_element(By.XPATH, locators.souces_button).click()
        # Ожидание появления заголовка "Соусы"
        header = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, locators.souces_header))
        )
        # Проверка видимости заголовка
        assert header.is_displayed(), "Header 'Соусы' is not displayed."

    def test_navigate_to_buns_with_scroll(self, driver):
        # Выполнение скролла вниз в окне конструктора
        constructor_menu = driver.find_element(By.XPATH, locators.constructor_window)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", constructor_menu)
        # Нажатие на кнопку "Булки"
        driver.find_element(By.XPATH, locators.buns_button).click()
        # Ожидание появления заголовка "Булки"
        header = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, locators.buns_header))
        )
        # Проверка видимости заголовка
        assert header.is_displayed(), "Header 'Булки' is not displayed."
