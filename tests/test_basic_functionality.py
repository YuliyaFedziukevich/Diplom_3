import allure
from data.url import main_url, url_orders_feed, url_detail_ingredients_bun_r_2
from pages.basic_functionality_pages import BasicFunctionalityPages

class TestBasicFunctionality:

    @allure.title('Успешный переход в раздел "Конструктор" по клику на "Конструктор" в шапке страницы')
    def test_successful_transfer_by_clicking_constructor_to_section_constructor(self, driver_feed):
        basic_functionality_pages = BasicFunctionalityPages(driver_feed)
        # Подождать, пока "Конструктор" станет кликабелен, нажать кнопку "Конструктор"
        basic_functionality_pages.wait_and_click_constructor()
        with allure.step('Проверка, что актуальная страница - главная, на которой расположен конструктор'):
            assert driver_feed.current_url == main_url

    @allure.title('Успешный переход в раздел "Лента заказов" по клику на "Ленту заказов" в шапке страницы')
    def test_successful_transfer_by_clicking_orders_feed_to_section_orders_feed(self, driver_main):
        basic_functionality_pages = BasicFunctionalityPages(driver_main)
        # Подождать, пока "Лента заказов" станет кликабельна, нажать "Лента заказов"
        basic_functionality_pages.wait_and_click_orders_feed()
        with allure.step('Проверка, что актуальная страница - "Лента заказов"'):
            assert driver_main.current_url == url_orders_feed

    @allure.title('Если кликнуть на ингредиент "Флюоресцентная булка R2-D3", появится всплывающее окно с деталями')
    def test_successful_appears_details_window_by_clicking_ingredient(self, driver_main):
        basic_functionality_pages = BasicFunctionalityPages(driver_main)
        # Кликнуть по ингредиенту "Флюоресцентная булка R2-D3"
        basic_functionality_pages.wait_and_click_bun_r_2()
        # Дождаться, когда будет видимым окно "Детали ингредиента" и проверить, что на нём отображается название ингредиента "Флюоресцентная булка R2-D3"
        basic_functionality_pages.wait_and_check_ingredient_details_of_fluorescent_bun()
        with allure.step('Проверка, что актуальная страница - "Детали ингредиента""Флюоресцентная булка R2-D3"'):
            assert driver_main.current_url == url_detail_ingredients_bun_r_2

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_successful_close_ingredients_details_by_click_close_button(self, driver_main):
        basic_functionality_pages = BasicFunctionalityPages(driver_main)
        # Дождаться, когда будет видимым окно "Детали ингредиента" и проверить, что на нём отображается название ингредиента "Флюоресцентная булка R2-D3"
        basic_functionality_pages.wait_and_click_bun_r_2()
        # Кликнуть по крестику на окне "Детали ингредиента"
        basic_functionality_pages.wait_and_click_close_button_on_ingredient_details()
        # Дождаться, что окно "Детали ингредиента" исчезнет
        basic_functionality_pages.wait_invisibility_ingredient_details()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredients_counter_increases_successful(self, driver_main):
        basic_functionality_pages = BasicFunctionalityPages(driver_main)
        # Найти первоначальное количество ингредиента "Соус фирменный Space Sauce"
        initial_quantity = int(basic_functionality_pages.find_ingredient_quantity())
        # Перетянуть ингредиент "Соус фирменный Space Sauce" в заказ
        basic_functionality_pages.transfer_ingredient_space_sauce_to_order(driver_main)
        # Найти окончательное количество ингредиента "Соус фирменный Space Sauce"
        last_quantity = int(basic_functionality_pages.find_ingredient_quantity())
        with allure.step('Проверка, что после добавления ингредиента в заказ счётчик этого ингредиента увеличился на 1'):
            assert last_quantity == initial_quantity + 1
