import pytest
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument('log-level=3')
    if platform != "win32":
        options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_buy_a_product(browser):
    home_page = HomePage(browser)
    home_page.load()

    assert home_page.get_number_of_products() == 6

    home_page.check_valid_links_of_products()
    home_page.check_valid_links_of_footer()
    home_page.check_valid_links_of_navbar()
