import pytest
from pages.register_page import RegisterPage
from data.user_data import REGISTER_USER


class TestRegistration:
    def test_create_account_success(self, driver):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.fill_registration_form(**REGISTER_USER)
        register_page.click_create_account()

        register_page.wait_for_signin_page()
        assert "/signin" in register_page.get_current_url()