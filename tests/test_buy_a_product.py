import pytest, time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage
from pages.product_page import Product
from pages.shipping_page import Shipping
from testdata.testdata_buy_product import testdata
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument('log-level=3')
    if platform != "win32":
        options.add_argument("--headless")
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
    assert product.get_value_of_items_in_cart() == "1"

    product.proceed_to_checkout()

    shipping_page = Shipping(browser)
    shipping_page.wait_for_loading_spinner()

    assert 'checkout/#shipping' in browser.current_url

    shipping_page.insert_text_in_input_field(testdata["email"], 'email')
    shipping_page.insert_text_in_input_field(testdata["first_name"], 'first_name')
    shipping_page.insert_text_in_input_field(testdata["last_name"], 'last_name')
    shipping_page.insert_text_in_input_field(testdata["street_address"], 'street_address')
    shipping_page.insert_text_in_input_field(testdata["city"], 'city')
    shipping_page.insert_text_in_input_field(testdata["post_code"], 'post_code') 
    shipping_page.insert_text_in_input_field(testdata["phone"], 'phone')   
    shipping_page.select_country('Romania')
    shipping_page.wait_for_loading_spinner()
    shipping_page.state_select('Cluj')
    shipping_page.wait_for_loading_spinner()
    shipping_page.select_ship_method()

    shipping_page.click_next()
    time.sleep(2)

    assert 'checkout/#payment' in browser.current_url

    time.sleep(4)