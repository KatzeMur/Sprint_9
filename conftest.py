import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.register_page import RegisterPage
from data.user_data import REGISTER_USER


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_test_user(driver):
    timestamp = int(time.time())
    user_data = REGISTER_USER.copy()
    user_data["username"] = f"{REGISTER_USER['username']}_{timestamp}"
    user_data["email"] = f"{timestamp}_{REGISTER_USER['email']}"
    
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.fill_registration_form(**user_data)
    register_page.click_create_account()
    WebDriverWait(driver, 10).until(EC.url_contains("/signin"))
    return user_data