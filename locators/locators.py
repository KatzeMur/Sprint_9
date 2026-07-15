# Локаторы для страницы регистрации
FIRST_NAME_INPUT = "//input[@name='first_name']"
LAST_NAME_INPUT = "//input[@name='last_name']"
USERNAME_INPUT = "//input[@name='username']"
EMAIL_INPUT = "//input[@name='email']"
PASSWORD_INPUT = "//input[@name='password']"
CREATE_ACCOUNT_BUTTON = "//button[text()='Создать аккаунт']"

# Локаторы для страницы входа
EMAIL_INPUT_LOGIN = "//input[@name='email']"
PASSWORD_INPUT_LOGIN = "//input[@name='password']"
LOGIN_BUTTON = "//form//button[text()='Войти']"
LOGOUT_BUTTON = "//a[text()='Выход']"

# Локаторы для страницы создания рецепта
CREATE_RECIPE_LINK = "//a[text()='Создать рецепт']"
RECIPE_NAME_INPUT = "(//input[@class='styles_inputField__3eqTj'])[1]"
INGREDIENTS_INPUT = "//input[contains(@class, 'styles_ingredientsInput')]"
INGREDIENT_DROPDOWN = "//div[contains(@class, 'container')]//div[text()='{}']"
INGREDIENT_AMOUNT_INPUT = "//input[contains(@class, 'styles_ingredientsAmountValue')]"
ADD_INGREDIENT_BUTTON = "//div[text()='Добавить ингредиент']"
COOKING_TIME_INPUT = "//div[text()='Время приготовления']/parent::label//input"
DESCRIPTION_TEXTAREA = "//textarea[contains(@class, 'styles_textareaField')]"
FILE_UPLOAD_INPUT = "//input[@type='file']"
CREATE_RECIPE_BUTTON = "//button[text()='Создать рецепт']"
RECIPE_PAGE_LOADED = "//div[@class='styles_inputLabelText__WsyhD' and text()='Название рецепта']"
RECIPE_CARD_TITLE = "//h1[contains(@class, 'styles_single-card__title') and text()='{}']"