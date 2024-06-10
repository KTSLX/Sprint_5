from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login


def test_logout_from_account_success(driver):
    # Создаём переменные с селекторами кнопок
    account_button = '//*[@id="root"]/div/header/nav/a/p'
    logout_button = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
    login_form_button = '//*[@id="root"]/div/main/div/form/button[text()="Войти"]'

    # Кликнуть на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]').click()

    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))

    # Логинимся и попадаем на главную
    login(driver)

    # Ожидание появления кнопки для перехода в личный кабинет
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, account_button)))

    # Кликнуть на кнопку "Личный кабинет" - отсюда будет осуществлён выход
    driver.find_element(By.XPATH, account_button).click()

    # Ожидание появления кнопки "Выход"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, logout_button)))

    # Кликнуть на кнопку выхода
    driver.find_element(By.XPATH, logout_button).click()

    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))

    # Ожидание появления кнопки "Войти" под формой логина и проверка, что мы на странице логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, login_form_button)))
    login_form_text = driver.find_element(By.XPATH, login_form_button).text
    assert login_form_text == "Войти"
