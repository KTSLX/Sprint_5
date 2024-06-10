from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(driver):
    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]')))
    # Ввод логина
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input[@type="text"]').send_keys('akuts9123@gmail.com')
    # Ввод пароля
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input[@type="password"]').send_keys('111111')
    # Клик по кнопке "Войти"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]').click()
    # Ожидание перехода на главную после успешного логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[text()="Соберите бургер"]')))
