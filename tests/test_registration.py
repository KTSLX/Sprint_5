# Набор тестов по регистрации нового пользователя
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_all_fields_registered(driver):
    # Кликнуть на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))

    # Кликнуть на кнопку "Регистрация" на странице входа - откроется форма регистрации
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
    # Ожидание появления кнопки "Зарегистрироваться"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Зарегистрироваться"]')))

    # Ввод имени
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Alexander')
    # Ввод email
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('akuts9' + str(random.randint(100, 999)) + '@gmail.com')
    # Ввод пароля
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('testpassword')
    # Клик на кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Зарегистрироваться"]').click()
    # Ожидание формы логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))

    #Проверка что регистрация произошла успешно
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')
    assert login_button is not None, "Registration failed: 'Войти' button not found."
    print("Регистрация произошла успешно и отображается страница логина.")

def test_registration_invalid_password_error_message(driver):
    # Кликнуть на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))

    # Кликнуть на кнопку "Регистрация" на странице входа - откроется форма регистрации
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
    # Ожидание появления кнопки "Зарегистрироваться"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Зарегистрироваться"]')))

    # Ввод имени
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Alexander')
    # Ввод email
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('akuts9' + str(random.randint(100, 999)) + '@gmail.com')
    # Ввод некорректного пароля - мало символов
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('testp')
    # Клик на кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Зарегистрироваться"]').click()
    # Ожидание появления ошибки
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p[text()="Некорректный пароль"]')))

    #Проверка правильности отображения сообщения об ошибке
    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p[text()="Некорректный пароль"]')
    assert error_message is not None, "Expected error message 'Некорректный пароль' not found."
    print("Сообщение об ошибке отображается корректно.")
