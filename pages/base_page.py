from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.url import main_url, url_orders_feed, url_detail_ingredients_bun_r_2

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # Поиск элемента
    def find(self, locator):
        return self.driver.find_element(*locator)

    # Поиск текста элемента
    def find_text(self, locator):
        return self.find(locator).text

    # Кликнуть найденный элемент
    def click(self, locator):
        self.find(locator).click()

    # Заполнить полн данными
    def send_keys(self, locator, data):
        self.find(locator).send_keys(data)

    # Дождаться, пока элемент будет кликабельным
    def wait_clickable(self, locators):
        return self.wait.until(expected_conditions.element_to_be_clickable(locators))

    # Дождаться, пока элемент будет кликабельным, и кликнуть его
    def wait_clickable_and_click(self, locator):
        return self.wait_clickable(locator).click()

    # Дождаться, пока элемент будет видимым
    def wait_visibility(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    # Дождаться, пока элемент будет видимый и отображенный
    def wait_visibility_and_displayed(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).is_displayed()

    # Дождаться, пока элемент будет видимый и доступный
    def wait_visibility_and_enabled(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).is_enabled()

    # Дождаться, пока элемент станет невидимым
    def wait_invisibility(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    # Переход на главную страницу
    @staticmethod
    def get_orders_feed_page(driver):
        driver.get(url_orders_feed)

    @staticmethod
    def drag_and_drop(driver, source, target):
        if driver.name == 'firefox':
            # need to simulate drag and drop functionality since the generic solution doesn't work in Firefox
            script = """
                    function simulateDragAndDrop(source, target) {
                        const dataTransfer = new DataTransfer();

                        function trigger(eventType, element) {
                                const event = new DragEvent(eventType, {
                                bubbles: true,
                                cancelable: true,
                                dataTransfer: dataTransfer,
                            });
                            element.dispatchEvent(event);
                        }

                        trigger('dragstart', source);
                        trigger('dragenter', target);
                        trigger('dragover', target);
                        trigger('drop', target);
                        trigger('dragend', source);
                    }            
                    simulateDragAndDrop(arguments[0], arguments[1]);
                    """
            driver.execute_script(script, source, target)
        else:
            ActionChains(driver).drag_and_drop(source, target).perform()

    @staticmethod
    # Проверка, что актуальная страница - главная, на которой расположен конструктор
    def check_if_main_page(driver):
        assert driver.current_url == main_url

    @staticmethod
    # Проверка, что актуальная страница - "Лента заказов"
    def check_if_orders_feed_page(driver):
        assert driver.current_url == url_orders_feed

    @staticmethod
    #Проверка, что актуальная страница - "Детали ингредиента""Флюоресцентная булка R2-D3"
    def check_if_buns_detail_page(driver):
        assert driver.current_url == url_detail_ingredients_bun_r_2

    @staticmethod
    # Закрытие окна с помощью Esc
    def escape(driver):
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()