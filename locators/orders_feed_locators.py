from selenium.webdriver.common.by import By

# Локаторы "Ленты заказов"
class OrdersFeedLocators:

    # Кнопка "Лента заказов"
    button_orders_feed = (By.XPATH, '//p[text()="Лента Заказов"]')

    # Кнопка "Личный кабинет"
    user_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Счётчик «Выполнено за всё время»
    completed_in_all_time = (By.XPATH, '//p[text()="Выполнено за все время:"]/parent::div/p[contains(@class, "OrderFeed_number")]')

    # Счётчик «Выполнено за сегодня»
    completed_today = (
    By.XPATH, '//p[text()="Выполнено за сегодня:"]/parent::div/p[contains(@class, "OrderFeed_number")]')

    # Список заказов в разделе "В работе"
    in_working = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]')

    # Кнопка "Войти в аккаунт" на главной странице
    button_sign_in_to_account = (By.XPATH, '//main//button[text()="Войти в аккаунт"]')

    # Кнопка "Оформить заказ" на главной странице
    button_place_an_order = (By.XPATH, '//main//button[text()="Оформить заказ"]')

    # Окно с идентификатором заказа
    orders_identification = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]')

    # Крестик на окне с идентификатором заказа
    close_button_on_orders_identification = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')

    # Номер заказа на окне с идентификатором заказа
    orders_number = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')

    # Номер заказа на окне с идентификатором заказа
    orders_number_not_9999 = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow") and not(text()="9999")]')

class LocatorsEntry:
    # Поле "Email" в разделе "Вход"
    sign_in_email = (By.NAME, 'name')

    # Поле "Пароль" в разделе "Вход"
    sign_in_password = (By.NAME, 'Пароль')

    # Кнопка "Вход"
    button_sign_in = (By.XPATH, '//form//button[text() ="Войти"]')

