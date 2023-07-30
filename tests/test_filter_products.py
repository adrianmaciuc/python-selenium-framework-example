import pytest
import time
import re
from pages.product_catalog import ProductCatalog
from tests.conftest import config_driver


@pytest.fixture
def browser():
    driver = config_driver()
    yield driver
    driver.quit()


def test_filter_products(browser):
    product_catalog = ProductCatalog(browser)
    product_catalog.load('women/tops-women/hoodies-and-sweatshirts-women.html')
    product_catalog.wait_for_page_to_load()

    assert product_catalog.get_number_of_products() == 12

    product_catalog.filter_shopping_option_by("Style")
    product_catalog.filter_subcategory_of_shopping_option_by("Hoodie")
    time.sleep(1)
    assert product_catalog.get_number_of_products() == 9

    product_catalog.filter_shopping_option_by("Price")
    product_catalog.filter_subcategory_of_shopping_option_by("$60.00")
    time.sleep(1)
    assert product_catalog.get_number_of_products() == 1


def test_sort_products_by_price(browser):
    product_catalog = ProductCatalog(browser)
    product_catalog.load('women/tops-women/tanks-women.html')
    value_before_sort = product_catalog.get_price_of_product_nth(1)
    time.sleep(1)

    product_catalog.sort_by('Price')
    value_after_sort = product_catalog.get_price_of_product_nth(1)

    time.sleep(1)

    assert int(re.sub(r'\..*|\$', '', value_before_sort)) > int(re.sub(r'\..*|\$', '', value_after_sort))