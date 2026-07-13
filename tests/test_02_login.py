import pytest
from pages.login_page import LoginPage


class TestLogin:
    def test_login_success(self, driver, create_test_user):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.fill_login_form(create_test_user["username"], create_test_user["password"])
        login_page.click_login()

        login_page.wait_for_logout_button()
        assert login_page.is_logout_button_displayed()