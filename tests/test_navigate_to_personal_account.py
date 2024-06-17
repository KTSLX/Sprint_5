from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_module import login
import locators

class TestPersonalAccount:

    def test_personal_account_from_main_page_opened(self, driver):
        # Кликнуть на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, locators.sign_in_button).click()

        # Выполнить логин
        login(driver)

        # Кликнуть на кнопку "Личный Кабинет"
        driver.find_element(By.XPATH, locators.account_button).click()

        # Ожидание появления описания страницы личного кабинета
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, locators.account_info_header))
        )

        # Проверка, что описание страницы личного кабинета корректное
        description = driver.find_element(By.XPATH, locators.account_info_header).text
        assert description == "В этом разделе вы можете изменить свои персональные данные", "Description text does not match the expected value."
