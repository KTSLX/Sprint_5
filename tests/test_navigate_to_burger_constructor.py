from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login
import pytest
import locators

class TestConstructorNavigation:

    def test_from_account_to_constructor_opened_with_constructor_button(self, driver):
        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()

        # Логинимся и попадаем на главную
        login(driver)

        # Ожидание появления кнопки для перехода в личный кабинет
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.account_button)))

        # Кликнуть на кнопку "Личный кабинет" - отсюда будет переход к конструктору
        driver.find_element(By.XPATH, locators.account_button).click()

        # Ожидание появления подтверждения, что мы в личном кабинете
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, locators.account_info_header)))

        # Ожидание появления кнопки перехода
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constructor_button)))

        # Нажимаем на кнопку "Конструктор"
        driver.find_element(By.XPATH, locators.constructor_button).click()

        # Ожидание перехода на главную
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))

        # Проверка, что заголовок на главной странице корректный
        header = driver.find_element(By.XPATH, locators.constuctor_header).text
        assert header == "Соберите бургер"

    def test_from_account_to_constructor_opened_with_stellar_burgers_button(self, driver):
        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()

        # Логинимся и попадаем на главную
        login(driver)

        # Ожидание появления кнопки для перехода в личный кабинет
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.account_button)))

        # Кликнуть на кнопку "Личный кабинет" - отсюда будет переход к конструктору
        driver.find_element(By.XPATH, locators.account_button).click()

        # Ожидание появления подтверждения, что мы в личном кабинете
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, locators.account_info_header)))

        # Ожидание появления кнопки перехода
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.stellar_burgers_button)))

        # Нажимаем на кнопку "Stellar Burgers"
        driver.find_element(By.XPATH, locators.stellar_burgers_button).click()

        # Ожидание перехода на главную
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))
