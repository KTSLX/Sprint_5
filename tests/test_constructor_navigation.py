from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

import locators


@pytest.mark.parametrize(
    "button_xpath, header_xpath, scroll_xpath",
    [
        (locators.fillings_button, locators.fillings_header, None),  # Начинки (без скролла)
        (locators.souces_button, locators.souces_header, None),  # Соусы (без скролла)
        (locators.buns_button, locators.buns_header, locators.constructor_window)  # Булки (со скроллом)
    ]
)
def test_constructor_navigation(driver, button_xpath, header_xpath, scroll_xpath):

    # Описываем условие для скролла (нужен для теста булок, т.к. булки видны изначально)
    if scroll_xpath:
        # Выполнение скролла вниз в окне конструктора
        constructor_menu = driver.find_element(By.XPATH, scroll_xpath)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", constructor_menu)

    # Нажатие на кнопку навигации
    driver.find_element(By.XPATH, button_xpath).click()

    # Ожидание появления соответствующего заголовка после скролла
    header = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, header_xpath))
    )

    # Проверка видимости заголовка
    assert header.is_displayed(), f"Header with xpath {header_xpath} is not displayed."
