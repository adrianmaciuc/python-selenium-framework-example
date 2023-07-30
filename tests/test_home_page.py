import pytest
from pages.home_page import HomePage
from tests.conftest import config_driver


@pytest.fixture
def browser():
    driver = config_driver()
    yield driver
    driver.quit()


def test_smoke_home_page(browser):
    home_page = HomePage(browser)
    home_page.load()

    assert home_page.get_number_of_products() == 6

    home_page.check_valid_links_of_products()
    home_page.check_valid_links_of_footer()
    home_page.check_valid_links_of_navbar()
