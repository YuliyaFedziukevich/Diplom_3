import allure
from pages.orders_feed_pages import OrdersFeedPages

class TestOrdersFeed:
    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_counter_in_completed_in_all_time_increases_successful(self, driver_feed):
        orders_feed_pages = OrdersFeedPages(driver_feed)
        # Проверить количество выполненных заказов за всё время
        initial_quantity = int(orders_feed_pages.check_orders_quantity_in_all_time())
        # Создание заказа c авторизацией пользователя через Личный кабинет
        orders_feed_pages.creating_order_with_user_authorization_via_user_account(driver_feed)
        # Перейти на страницу "Лента заказов"
        orders_feed_pages.get_orders_feed_page(driver_feed)
        # Проверить количество выполненных заказов за всё время
        last_quantity = int(orders_feed_pages.check_orders_quantity_in_all_time())
        with allure.step('Проверка, что после создания нового заказа счётчик "Выполнено за всё время" увеличивается'):
            assert last_quantity > initial_quantity

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_counter_in_completed_today_increases_successful(self, driver_feed):
        orders_feed_pages = OrdersFeedPages(driver_feed)
        # Проверить количество выполненных заказов за сегодня
        initial_quantity = int(orders_feed_pages.check_orders_quantity_today())
        # Создание заказа c авторизацией пользователя через Личный кабинет
        orders_feed_pages.creating_order_with_user_authorization_via_user_account(driver_feed)
        # Перейти на страницу "Лента заказов"
        orders_feed_pages.get_orders_feed_page(driver_feed)
        # Проверить количество выполненных заказов за всё время
        last_quantity = int(orders_feed_pages.check_orders_quantity_today())
        with allure.step('Проверка, что после создания нового заказа счётчик "Выполнено за сегодня" увеличивается'):
            assert last_quantity > initial_quantity

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_orders_number_after_creating_appears_in_section_in_progress(self, driver_main):
        orders_feed_pages = OrdersFeedPages(driver_main)
        # Создание заказа с авторизацией пользователя через "Войти в аккаунт" на главной странице
        # Получение номера заказа
        number = orders_feed_pages.creating_order_with_user_authorization_via_main_page(driver_main)
        # Перейти на страницу "Лента заказов"
        orders_feed_pages.get_orders_feed_page(driver_main)
        # Получение списка заказов "В работе"
        orders_list = orders_feed_pages.get_list_of_orders_in_work()
        with allure.step('Проверка, что после оформления заказа его номер появляется в разделе "В работе"'):
            assert number in orders_list
