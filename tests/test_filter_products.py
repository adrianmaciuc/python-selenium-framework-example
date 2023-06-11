import pytest
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.product_catalog import ProductCatalog
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


def test_filter_products(browser):
    product_catalog = ProductCatalog(browser)
    product_catalog.load('women/tops-women/hoodies-and-sweatshirts-women.html')
    product_catalog.wait_for_page_to_load()

    assert product_catalog.get_number_of_products() == 12

    product_catalog.select_filter_option_by_text("Style")
    # product_catalog.select_filter_subcategory_option_by_text("Hoodie")
    product_catalog.wait_for_page_to_load()

    assert product_catalog.get_number_of_products() == 9

    product_catalog.select_filter_option_by_text("Price")
    # product_catalog.select_filter_subcategory_option_by_text("$60.00 and above")
    product_catalog.wait_for_page_to_load()

    assert product_catalog.get_number_of_products() == 1
