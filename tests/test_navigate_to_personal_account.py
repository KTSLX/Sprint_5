from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login


def test_personal_account_from_main_page_opened(driver):
    # Кликнуть на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]').click()

    # Выполнить логин
    login(driver)

    # Кликнуть на кнопку "Личный Кабинет"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p[text()="Личный Кабинет"]').click()

    # Ожидание появления описания страницы личного кабинета
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/p[text()="В этом разделе вы можете изменить свои персональные данные"]'))
    )

    # Проверка, что описание страницы личного кабинета корректное
    description = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/p[text()="В этом разделе вы можете изменить свои персональные данные"]').text
    assert description == "В этом разделе вы можете изменить свои персональные данные", "Description text does not match the expected value."
    print("Тест успешно выполнен.")
