import allure
from pages.base_page import BasePage
from locators.basic_functionality_locators import BasicFunctionalityLocators
from locators.ingredients_locators import IngredientsLocators

class BasicFunctionalityPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать "Конструктор"')
    def wait_and_click_constructor(self):
        # Подождать, пока "Конструктор" станет кликабелен, нажать кнопку "Конструктор"
        self.wait_clickable_and_click(BasicFunctionalityLocators.button_constructor_in_user_account)

    @allure.step('Нажать "Лента заказов"')
    def wait_and_click_orders_feed(self):
        # Подождать, пока "Лента заказов" станет кликабельна, нажать "Лента заказов"
        self.wait_clickable_and_click(BasicFunctionalityLocators.button_orders_feed)

    @allure.step('Клик по ингредиенту "Флюоресцентная булка R2-D3"')
    def wait_and_click_bun_r_2(self):
        # Подождать, пока "Флюоресцентная булка R2-D3" станет кликабельна, нажать "Флюоресцентная булка R2-D3"
        self.wait_clickable_and_click(IngredientsLocators.fluorescent_bun)

    @allure.step('Дождаться, когда будет видимым окно "Детали ингредиента" и проверить, что на нём отображается название ингредиента "Флюоресцентная булка R2-D3"')
    def wait_and_check_ingredient_details_of_fluorescent_bun(self):
        ingredients_name = self.find_text(BasicFunctionalityLocators.ingredients_name_on_details_on_ingredients_details)
        assert self.wait_visibility_and_displayed(BasicFunctionalityLocators.ingredients_details)
        assert self.wait_visibility_and_enabled(BasicFunctionalityLocators.ingredients_name_on_details_on_ingredients_details)
        assert ingredients_name == "Флюоресцентная булка R2-D3"

    @allure.step('Клик по крестику на окне "Детали ингредиента"')
    def wait_and_click_close_button_on_ingredient_details(self):
        # Подождать, пока крестик на окне "Детали ингредиента" станет кликабельным, кликнуть по крестику
        self.wait_clickable_and_click(BasicFunctionalityLocators.close_button_ingredients_details)

    @allure.step('Дождаться, что окно "Детали ингредиента" исчезнет')
    def wait_invisibility_ingredient_details(self):
        self.wait_invisibility(BasicFunctionalityLocators.ingredients_details)

    @allure.step('Дождаться, что ингредиент "Соус фирменный Space Sauce" станет видимым')
    def find_and_wait_visibility_space_sauce(self):
        return self.wait_visibility(IngredientsLocators.space_sauce)

    @allure.step('Найти количество ингредиента "Соус фирменный Space Sauce"')
    def find_ingredient_quantity(self):
        return self.find_text(IngredientsLocators.space_sauce_counter)

    @allure.step('Перетянуть ингредиент "Соус фирменный Space Sauce" в заказ')
    def transfer_ingredient_space_sauce_to_order(self, driver):
        basket_area = self.find(IngredientsLocators.burger_constructor_basket)
        sauce_element = self.find_and_wait_visibility_space_sauce()
        self.drag_and_drop(driver, sauce_element, basket_area)