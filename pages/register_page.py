from locators.locators import (
    FIRST_NAME_INPUT,
    LAST_NAME_INPUT,
    USERNAME_INPUT,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    CREATE_ACCOUNT_BUTTON
)
from data.constants import BASE_URL
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def open(self):
        self.driver.get(f"{BASE_URL}/signup")

    def fill_registration_form(self, first_name, last_name, username, email, password):
        self.input_text(FIRST_NAME_INPUT, first_name)
        self.input_text(LAST_NAME_INPUT, last_name)
        self.input_text(USERNAME_INPUT, username)
        self.input_text(EMAIL_INPUT, email)
        self.input_text(PASSWORD_INPUT, password)

    def click_create_account(self):
        self.click(CREATE_ACCOUNT_BUTTON)

    def wait_for_signin_page(self):
        self.wait_url_contains("/signin")

    def get_current_url(self):
        return super().get_current_url()