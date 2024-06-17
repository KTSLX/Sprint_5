from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import locators
import data_module
def login(driver):
    # Ожидание появления кнопки "Войти" под формой логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_button_on_login_page)))
    # Ввод логина
    driver.find_element(By.XPATH, locators.email_input_field).send_keys(data_module.login_email)
    # Ввод пароля
    driver.find_element(By.XPATH, locators.password_input_field).send_keys(data_module.login_password)
    # Клик по кнопке "Войти"
    driver.find_element(By.XPATH, locators.sign_in_button_on_login_page).click()
    # Ожидание перехода на главную после успешного логина
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, locators.constuctor_header)))
