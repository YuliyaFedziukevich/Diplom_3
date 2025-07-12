import allure
from pages.base_page import BasePage
from data.user_data import UserData
from locators.ingredients_locators import IngredientsLocators
from locators.orders_feed_locators import OrdersFeedLocators, LocatorsEntry

orders_feed_locators = OrdersFeedLocators()
locators_entry = LocatorsEntry()

class OrdersFeedPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение полей раздела "Вход" существующими данными')
    def fill_sign_in_fields(self):
        self.wait_clickable(locators_entry.button_sign_in)
        self.send_keys(locators_entry.sign_in_email, UserData.user_email)
        self.send_keys(locators_entry.sign_in_password, UserData.user_password)
        self.click(locators_entry.button_sign_in)

    @allure.step('Войти в аккаунт')
    def sign_in_main_page(self):
        # Дождаться, пока будет кликабельна кнопка "Войти в аккаунт" на главной странице и кликнуть на неё
        self.wait_clickable_and_click(orders_feed_locators.button_sign_in_to_account)
        # Заполнить поля "Email" и "Пароль", нажать кнопку "Войти" на экране "Вход"
        self.fill_sign_in_fields()

    @allure.step('Войти в Личный кабинет')
    def sign_in_orders_feed(self):
        # Дождаться, пока будет кликабельна кнопка "Войти в аккаунт" на главной странице и кликнуть на неё
        self.wait_clickable_and_click(orders_feed_locators.user_account)
        # Заполнить поля "Email" и "Пароль", нажать кнопку "Войти" на экране "Вход"
        self.fill_sign_in_fields()

    @allure.step('Оформление заказа')
    def creating_order(self, driver, buns, sauce_element, filling):
        # Найти корзину заказа
        basket_area = self.wait_visibility(IngredientsLocators.burger_constructor_basket)
        # Перенести ингредиенты в корзину
        self.drag_and_drop(driver, buns, basket_area)
        self.drag_and_drop(driver, filling, basket_area)
        self.drag_and_drop(driver, sauce_element, basket_area)
        # Дождаться, пока будет кликабельна кнопка "Оформить заказ" на главной странице и кликнуть на неё
        self.wait_clickable_and_click(orders_feed_locators.button_place_an_order)
        # Дождаться, пока отобразится окно "Идентификатор заказа"
        self.wait_visibility_and_displayed(orders_feed_locators.orders_identification)
        # Получение номера заказа
        order_number = self.get_orders_number()
        # Закрыть окно "Идентификатор заказа"
        self.escape(driver)
        return order_number

    @allure.step('Создание заказа c выбранными ингредиентами для теста - булочкой, начинкой и соусом')
    def order_creation(self, driver):
        # Выбор конкретных ингредиентов для заказа
        buns = self.wait_clickable(IngredientsLocators.fluorescent_bun)
        sauce_element = self.wait_clickable(IngredientsLocators.space_sauce)
        filling = self.wait_clickable(IngredientsLocators.filling_meat)
        # Оформление заказа c выбранными ингредиентами для теста
        return self.creating_order(driver, buns, sauce_element, filling)

    @allure.step('Создание заказа c авторизацией пользователя через Личный кабинет')
    def creating_order_with_user_authorization_via_user_account(self, driver):
        # Войти в аккаунт
        self.sign_in_orders_feed()
        # Оформить заказ
        return self.order_creation(driver)

    @allure.step('Создание заказа c авторизацией пользователя через "Войти в аккаунт" на главной странице')
    def creating_order_with_user_authorization_via_main_page(self, driver):
        # Войти в аккаунт
        self.sign_in_main_page()
        # Оформить заказ
        return self.order_creation(driver)

    @allure.step('Получение номера заказа')
    def get_orders_number(self):
        return self.wait_visibility(OrdersFeedLocators.orders_number_not_9999).text

    @allure.step('Нажать "Лента заказов"')
    def wait_and_click_orders_feed(self):
        # Подождать, пока "Лента заказов" станет кликабельна, нажать "Лента заказов"
        self.wait_clickable_and_click(OrdersFeedLocators.button_orders_feed)

    @allure.step('Проверить количество выполненных заказов за всё время')
    def check_orders_quantity_in_all_time(self):
        # Дождаться, пока счётчик "Выполнено за всё время" будет видимый
        self.wait_visibility(OrdersFeedLocators.completed_in_all_time)
        return self.find_text(OrdersFeedLocators.completed_in_all_time)

    @allure.step('Проверить количество выполненных заказов за сегодня')
    def check_orders_quantity_today(self):
        # Дождаться, пока счётчик "Выполнено за сегодня" будет видимый
        self.wait_visibility(OrdersFeedLocators.completed_today)
        return self.find_text(OrdersFeedLocators.completed_today)

    @allure.step('Получение списка заказов "В работе"')
    def get_list_of_orders_in_work(self):
        # Дождаться, пока "В работе" будет видимый
        self.wait_visibility(OrdersFeedLocators.in_working)
        return self.find_text(OrdersFeedLocators.in_working)
