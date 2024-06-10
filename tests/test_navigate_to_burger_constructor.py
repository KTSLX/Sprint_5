from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login
import pytest


@pytest.mark.parametrize(
    'constructor_button',
    [
        '//*[@id="root"]/div/header/nav/ul/li[1]/a/p',  # кнопка "Конструктор"
        '//*[@id="root"]/div/header/nav/div/a'  # кнопка "Stellar Burgers"
    ]
)
def test_from_account_to_constructor_opened(driver, constructor_button):
    # Создаём переменную с селектором кнопки личного кабинета
    account_button = '//*[@id="root"]/div/header/nav/a/p'

    # Кликнуть на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]').click()

    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))

    # Логинимся и попадаем на главную
    login(driver)

    # Ожидание появления кнопки для перехода в личный кабинет
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, account_button)))

    # Кликнуть на кнопку "Личный кабинет" - отсюда будет переход к конструктору
    driver.find_element(By.XPATH, account_button).click()

    # Ожидание появления подтверждения, что мы в личном кабинете
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/div/nav/p[text()="В этом разделе вы можете изменить свои персональные данные"]')))

    # Ожидание появления кнопки перехода
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, constructor_button)))

    # Нажимаем на кнопку "Конструктор" / "StellarBurgers"
    driver.find_element(By.XPATH, constructor_button).click()

    # Ожидание перехода на главную
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[text()="Соберите бургер"]')))

    # Проверка, что заголовок на главной странице корректный
    header = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[text()="Соберите бургер"]').text
    assert header == "Соберите бургер"
    print('Тест выполнен успешно')
