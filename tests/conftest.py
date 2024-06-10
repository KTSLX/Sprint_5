import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Войти в аккаунт"]')))
    yield driver
    driver.quit()
