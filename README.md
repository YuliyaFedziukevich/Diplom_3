**Тестовые сценарии**:
* 1 "Основная функциональность"
* 2 "Лента заказов"

**Перечень папок и файлов**:
* 1 **data**:
* - url.py -  перечень используемых при тестировании url;
* - user_data.py - файл с существующими данными пользователя для авторизации;
* 2 **locators**:
* - basic_functionality_locators.py - локаторы для тестирования основной функциональности;
* - ingredients_locators.py - локаторы ингредиентов;
* - orders_feed_locators.py - локаторы "Ленты заказов";
* 3 **pages**:
* - base_page - общие методы для тестирования;
* - basic_functionality_pages.py - методы для тестирования основной функциональности;
* - orders_feed_pages.py - методы для тестирования "Ленты заказов";
* 4 **tests**:
* - test_basic_functionality.py - тесты по основной функциональности:
*   -- test_successful_transfer_by_clicking_constructor_to_section_constructor;
*   -- test_successful_transfer_by_clicking_orders_feed_to_section_orders_feed;
*   -- test_successful_appears_details_window_by_clicking_ingredient;
*   -- test_successful_close_ingredients_details_by_click_close_button;
*   -- test_ingredients_counter_increases_successful
* - test_orders_feed.py - тесты "Ленты заказов":
*   --test_counter_in_completed_in_all_time_increases_successful;
*   -- test_counter_in_completed_today_increases_successful;
*   -- test_orders_number_after_creating_appears_in_section_in_progress;
* 5 **conftest.py** - содержит фикстуры; 
* 6 **requirements.txt** - файл с внешними зависимостями;
* 7 **allure_report** - сгенерированный Allure-отчёт