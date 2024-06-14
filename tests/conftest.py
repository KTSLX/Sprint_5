import pytest
from selenium import webdriver
from config import BASE_URL

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()