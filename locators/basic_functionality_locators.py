from selenium.webdriver.common.by import By

# Локаторы главной страницы
class BasicFunctionalityLocators:

    # Кнопка "Конструктор"
    button_constructor_in_user_account = (By.XPATH, '//p[text()="Конструктор"]')

    # Кнопка "Лента заказов"
    button_orders_feed = (By.XPATH, '//p[text()="Лента Заказов"]')

    # Всплывающее окно "Детали ингредиента"
    ingredients_details = (By.XPATH, '//h2[text() = "Детали ингредиента"]')

    # Название ингредиента на окне "Детали ингредиента"
    ingredients_name_on_details_on_ingredients_details = (By.XPATH,'//h2[text() = "Детали ингредиента"]/ancestor::section/div/div/p')

    # Крестик в окне "Детали ингредиента"
    close_button_ingredients_details = (By.XPATH, '//h2[text() = "Детали ингредиента"]/ancestor::section/div/button')
