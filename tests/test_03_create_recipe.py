import os
import time
import allure
import pytest
from pages.recipe_page import RecipePage
from pages.login_page import LoginPage


class TestCreateRecipe:
    @allure.title("Создание рецепта")
    def test_create_recipe_success(self, driver, create_test_user):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.fill_login_form(create_test_user["username"], create_test_user["password"])
        login_page.click_login()
        login_page.wait_for_logout_button()

        recipe_page = RecipePage(driver)
        recipe_page.open()
        recipe_page.wait_for_recipe_page()

        timestamp = int(time.time())
        recipe_name = f"Тестовый рецепт {timestamp}"
        photo_path = os.path.abspath("assets/tomato-isolated_2829-17583.jpg")

        recipe_page.fill_recipe_name(recipe_name)
        recipe_page.add_ingredient("картофель", "10")
        recipe_page.click_add_ingredient()
        recipe_page.set_cooking_time("30")
        recipe_page.fill_description("Тестовое описание рецепта")
        recipe_page.upload_photo(photo_path)
        recipe_page.click_create()

        assert recipe_page.is_recipe_created(recipe_name)
        