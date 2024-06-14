from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login
import pytest
import locators


@pytest.mark.parametrize(
    'constructor_button',
    [
        locators.constructor_button,  # кнопка "Конструктор"
        locators.stellar_burgers_button  # кнопка "Stellar Burgers"
    ]
)
def test_from_account_to_constructor_opened(driver, constructor_button):

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
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, constructor_button)))

    # Нажимаем на кнопку "Конструктор" / "StellarBurgers"
    driver.find_element(By.XPATH, constructor_button).click()

    # Ожидание перехода на главную
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))

    # Проверка, что заголовок на главной странице корректный
    header = driver.find_element(By.XPATH, locators.constuctor_header).text
    assert header == "Соберите бургер"
