import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login


@pytest.mark.parametrize(
    'test_type, login_button, login_start_page',
    [
        ('main_page', '//*[@id="root"]/div/header/nav/a/p[text()="Личный Кабинет"]', None),
        ('main_page', '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]', None),
        ('registration_page', '//*[@id="root"]/div/main/div/div/p[text()="Уже зарегистрированы?"]/a[text()="Войти"]',
         '//*[@id="root"]/div/main/div/div/p[1]/a[text()="Зарегистрироваться"]'),
        ('recovery_page', '//*[@id="root"]/div/main/div/div/p[text()="Вспомнили пароль?"]/a[text()="Войти"]',
         '//*[@id="root"]/div/main/div/div/p[2]/a[text()="Восстановить пароль"]')
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
        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]').click()
        # Ожидание появления кнопки "Войти" под формой логина
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))
        # Кликнуть по кнопке "Зарегистрироваться" или "Восстановить пароль"
        driver.find_element(By.XPATH, login_start_page).click()
        # Ожидание кнопки "Войти"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, login_button)))
        # Клик по кнопке "Войти"
        driver.find_element(By.XPATH, login_button).click()

    # Логинимся
    login(driver)

    # Проверка что логин произошёл успешно
    main_page_header = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[text()="Соберите бургер"]'))
    )
    assert main_page_header is not None, "Login failed: 'Соберите бургер' header not found."
    print("Login успешен и отображается главная страница.")
