import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import (
    CREATE_RECIPE_LINK,
    RECIPE_NAME_INPUT,
    INGREDIENTS_INPUT,
    INGREDIENT_DROPDOWN,
    INGREDIENT_AMOUNT_INPUT,
    ADD_INGREDIENT_BUTTON,
    COOKING_TIME_INPUT,
    DESCRIPTION_TEXTAREA,
    FILE_UPLOAD_INPUT,
    CREATE_RECIPE_BUTTON,
    RECIPE_CARD_TITLE,
    RECIPE_PAGE_LOADED,
    LOGOUT_BUTTON
)
from data.constants import BASE_URL
from pages.base_page import BasePage


class RecipePage(BasePage):
    def open(self):
        self.driver.get(f"{BASE_URL}/recipes/create")

    @allure.step("Заполнение названия рецепта")
    def fill_recipe_name(self, name):
        self.input_text(RECIPE_NAME_INPUT, name)

    @allure.step("Добавление ингредиента")
    def add_ingredient(self, ingredient_name, amount="1"):
        input_field = self.find_element(INGREDIENTS_INPUT)
        input_field.clear()
        input_field.send_keys(ingredient_name)
        
        self.wait_for_element(f"//div[text()='{ingredient_name}']")
        
        dropdown_option = self.find_element(INGREDIENT_DROPDOWN.format(ingredient_name))
        dropdown_option.click()
        
        amount_field = self.find_element(INGREDIENT_AMOUNT_INPUT)
        amount_field.clear()
        amount_field.send_keys(amount)

    @allure.step("Нажатие кнопки 'Добавить ингредиент'")
    def click_add_ingredient(self):
        self.click(ADD_INGREDIENT_BUTTON)

    @allure.step("Заполнение времени приготовления")
    def set_cooking_time(self, minutes):
        self.input_text(COOKING_TIME_INPUT, minutes)

    @allure.step("Заполнение описания рецепта")
    def fill_description(self, text):
        self.input_text(DESCRIPTION_TEXTAREA, text)

    @allure.step("Загрузка фото")
    def upload_photo(self, file_path):
        self.find_element(FILE_UPLOAD_INPUT).send_keys(file_path)

    @allure.step("Нажатие кнопки 'Создать рецепт'")
    def click_create(self):
        self.click(CREATE_RECIPE_BUTTON)

    @allure.step("Ожидание загрузки страницы создания рецепта")
    def wait_for_recipe_page(self):
        self.wait_for_element(RECIPE_PAGE_LOADED)

    @allure.step("Ожидание карточки созданного рецепта")
    def wait_for_recipe_card(self, recipe_name):
        self.wait_for_visibility(RECIPE_CARD_TITLE.format(recipe_name))

    @allure.step("Проверка создания рецепта")
    def is_recipe_created(self, recipe_name):
        self.wait_for_visibility(RECIPE_CARD_TITLE.format(recipe_name))
        return True

    @allure.step("Ожидание кнопки 'Выход'")
    def wait_for_logout_button(self):
        self.wait_for_visibility(LOGOUT_BUTTON)
        