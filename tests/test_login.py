import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login
import locators


@pytest.mark.parametrize(
    'test_type, login_button, login_start_page',
    [
        ('main_page', locators.account_button, None),
        ('main_page', locators.sign_in_button, None),
        ('registration_page', locators.sign_in_button_on_registration_page, locators.registration_button_on_login_page),
        ('recovery_page', locators.sign_in_button_on_recovery_page, locators.recovery_button_on_login_page)
    ]
)
def test_login_different_start_points_logged_in(driver, test_type, login_button, login_start_page):
    if test_type == 'main_page':
        # Ожидание появления кнопки для перехода к форме логина
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, login_button)))
        # Кликнуть на кнопку "Войти в аккаунт"/"Личный кабинет"
        driver.find_element(By.XPATH, login_button).click()
    else:
        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        # Ожидание появления кнопки "Войти" под формой логина
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))
        # Кликнуть по кнопке "Зарегистрироваться" или "Восстановить пароль"
        driver.find_element(By.XPATH, login_start_page).click()
        # Ожидание кнопки "Войти"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, login_button)))
        # Клик по кнопке "Войти"
        driver.find_element(By.XPATH, login_button).click()

    # Логинимся (модуль login_module)
    login(driver)

    # Проверка что логин произошёл успешно
    main_page_header = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))
    assert main_page_header is not None, "Login failed: 'Соберите бургер' header not found."

