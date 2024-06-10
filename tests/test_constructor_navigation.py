from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login


def test_constructor_navigation_scrolls(driver):
    # Нажатие на кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]').click()
    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))
    # Логинимся и попадаем на главную
    login(driver)

    # Нажатие на кнопку "Начинки"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
    # Ожидание скролла до начинок
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')))

    # Нажатие на кнопку "Соусы"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
    # Ожидание скролла до соусов
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]')))

    # Нажатие на кнопку "Булки"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
    # Ожидание скролла до булок
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')))
