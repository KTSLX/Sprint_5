import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import data_module

def test_registration_all_fields_registered(driver):
    # Кликнуть на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, locators.sign_in_button).click()

    # Кликнуть на кнопку "Регистрация" на странице входа - откроется форма регистрации
    driver.find_element(By.XPATH, locators.registration_button_on_login_page).click()
    # Ожидание появления кнопки "Зарегистрироваться"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.registration_in_form_button)))

    # Ввод имени
    driver.find_element(By.XPATH, locators.registration_name_input).send_keys(data_module.registration_name)
    # Ввод email
    driver.find_element(By.XPATH, locators.registration_email_input).send_keys(data_module.registration_email)
    # Ввод пароля
    driver.find_element(By.XPATH, locators.registration_password_input).send_keys(data_module.registration_password)
    # Клик на кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, locators.registration_in_form_button).click()
    # Ожидание формы логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))

    #Проверка что регистрация произошла успешно
    login_button = driver.find_element(By.XPATH, locators.sign_in_button_on_login_page)
    assert login_button is not None, "Registration failed: 'Войти' button not found."


def test_registration_invalid_password_error_message(driver):
    # Кликнуть на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, locators.sign_in_button).click()

    # Кликнуть на кнопку "Регистрация" на странице входа - откроется форма регистрации
    driver.find_element(By.XPATH, locators.registration_button_on_login_page).click()
    # Ожидание появления кнопки "Зарегистрироваться"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.registration_in_form_button)))

    # Ввод имени
    driver.find_element(By.XPATH, locators.registration_name_input).send_keys(data_module.registration_name)
    # Ввод email
    driver.find_element(By.XPATH, locators.registration_email_input).send_keys(data_module.registration_email)
    # Ввод некорректного пароля - мало символов
    driver.find_element(By.XPATH, locators.registration_password_input).send_keys(data_module.registration_invalid_password)
    # Клик на кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, locators.registration_in_form_button).click()
    # Ожидание появления ошибки
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.registration_form_error)))

    #Проверка правильности отображения сообщения об ошибке
    error_message = driver.find_element(By.XPATH, locators.registration_form_error)
    assert error_message is not None, "Expected error message 'Некорректный пароль' not found."

