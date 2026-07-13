from locators.locators import (
    EMAIL_INPUT_LOGIN,
    PASSWORD_INPUT_LOGIN,
    LOGIN_BUTTON,
    LOGOUT_BUTTON
)
from data.constants import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.driver.get(f"{BASE_URL}/signin")

    def fill_login_form(self, email, password):
        self.input_text(EMAIL_INPUT_LOGIN, email)
        self.input_text(PASSWORD_INPUT_LOGIN, password)

    def click_login(self):
        self.click(LOGIN_BUTTON)

    def wait_for_logout_button(self):
        self.wait_for_visibility(LOGOUT_BUTTON)

    def is_logout_button_displayed(self):
        return self.is_element_displayed(LOGOUT_BUTTON)