from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login
import locators

class TestLogin:
    def test_login_from_account_button(self, driver):
        # Ожидание появления кнопки "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.account_button)))
        # Кликнуть на кнопку "Личный кабинет"
        driver.find_element(By.XPATH, locators.account_button).click()
        # Логинимся (модуль login_module)
        login(driver)
        # Проверка, что логин произошёл успешно
        main_page_header = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))
        assert main_page_header is not None, "Login failed: 'Соберите бургер' header not found."

    def test_login_from_main_page_sign_in_button(self, driver):
        # Ожидание появления кнопки "Войти в аккаунт"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button)))
        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        # Логинимся (модуль login_module)
        login(driver)
        # Проверка что логин произошёл успешно
        main_page_header = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))
        assert main_page_header is not None, "Login failed: 'Соберите бургер' header not found."

    def test_login_from_registration_page(self, driver):
        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        # Ожидание появления кнопки "Войти" под формой логина
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))
        # Кликнуть по кнопке "Зарегистрироваться"
        driver.find_element(By.XPATH, locators.registration_button_on_login_page).click()
        # Ожидание кнопки "Войти"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_registration_page)))
        # Клик по кнопке "Войти"
        driver.find_element(By.XPATH, locators.sign_in_button_on_registration_page).click()
        # Логинимся (модуль login_module)
        login(driver)
        # Проверка что логин произошёл успешно
        main_page_header = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))
        assert main_page_header is not None, "Login failed: 'Соберите бургер' header not found."

    def test_login_from_recovery_page(self, driver):
        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        # Ожидание появления кнопки "Войти" под формой логина
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))
        # Кликнуть по кнопке "Восстановить пароль"
        driver.find_element(By.XPATH, locators.recovery_button_on_login_page).click()
        # Ожидание кнопки "Войти"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_recovery_page)))
        # Клик по кнопке "Войти"
        driver.find_element(By.XPATH, locators.sign_in_button_on_recovery_page).click()
        # Логинимся (модуль login_module)
        login(driver)
        # Проверка что логин произошёл успешно
        main_page_header = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))
        assert main_page_header is not None, "Login failed: 'Соберите бургер' header not found."
