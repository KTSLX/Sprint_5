from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login
import locators

class TestLogout:

    def test_logout_from_account_success(self, driver):

        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()

        # Ожидание появления кнопки "Войти" под формой логина
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))

        # Логинимся и попадаем на главную
        login(driver)

        # Ожидание появления кнопки для перехода в личный кабинет
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.account_button)))

        # Кликнуть на кнопку "Личный кабинет" - отсюда будет осуществлён выход
        driver.find_element(By.XPATH, locators.account_button).click()

        # Ожидание появления кнопки "Выход"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.logout_button)))

        # Кликнуть на кнопку выхода
        driver.find_element(By.XPATH, locators.logout_button).click()

        # Ожидание появления кнопки "Войти" под формой логина
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))

        # Ожидание появления кнопки "Войти" под формой логина и проверка, что мы на странице логина
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))
        login_form_text = driver.find_element(By.XPATH, locators.sign_in_button_on_login_page).text
        assert login_form_text == "Войти"
