import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage
from pages.product import Product
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument('log-level=3')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_buy_a_product(browser):
    home_page = HomePage(browser)
    home_page.load()
    home_page.click_on_nth_product_item(1)

    product = Product(browser)
    product.choose_size('S')
    product.choose_color('blue')
    product.click_add_to_cart()

    assert product.add_to_cart_success_msg_visible() == True
    time.sleep(5)