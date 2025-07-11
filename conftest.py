import pytest
from selenium import webdriver
from data.url import main_url, url_orders_feed

@pytest.fixture(params=["Chrome", "Firefox"])
def driver_main(request):
    browser = request.param
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(main_url)
    yield driver
    driver.quit()

@pytest.fixture(params=["Chrome", "Firefox"])
def driver_feed(request):
    browser = request.param
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url_orders_feed)
    yield driver
    driver.quit()

