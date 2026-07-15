from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        element.click()

    def input_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )

    def wait_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(EC.url_contains(text))

    def get_current_url(self):
        return self.driver.current_url

    def is_element_displayed(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        return element.is_displayed()
    