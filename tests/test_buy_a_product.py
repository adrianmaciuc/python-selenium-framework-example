import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage
from pages.product_page import Product
from pages.shipping_page import Shipping
from pages.payment_page import Payment
from pages.checkout_success_page import Checkout
from testdata.testdata_buy_product import testdata
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()
                        ), options=options)
    yield driver
    driver.quit()


def test_buy_a_product(browser):
    home_page = HomePage(browser)

    # open home url
    home_page.load()

    # not able to intercept network calls

    # open nth product from home page
    home_page.click_on_nth_product_item(1)

    product = Product(browser)
    product.wait_for_page_to_load()
    product.choose_size('S')
    product.choose_color('orange')

    product.click_add_to_cart()
    assert product.add_to_cart_success_msg_visible()

    # assert number of items in cart
    assert product.get_value_of_items_in_cart() == "1"

    product.proceed_to_checkout()

    shipping_page = Shipping(browser)
    shipping_page.wait_for_page_to_load()

    assert 'checkout/#shipping' in shipping_page.browser.current_url

    # fill in the info for shipping
    shipping_page.insert_text_in_input_field(testdata["email"], 'email')
    shipping_page.insert_text_in_input_field(testdata["first_name"], 'first_name')
    shipping_page.insert_text_in_input_field(testdata["last_name"], 'last_name')
    shipping_page.insert_text_in_input_field(testdata["street_address"], 'street_address')
    shipping_page.insert_text_in_input_field(testdata["city"], 'city')
    shipping_page.insert_text_in_input_field(testdata["post_code"], 'post_code')
    shipping_page.insert_text_in_input_field(testdata["phone"], 'phone')
    shipping_page.select_country(testdata["country"])
    shipping_page.wait_for_loading_spinner()
    shipping_page.state_select(testdata["state"])
    shipping_page.wait_for_loading_spinner()
    shipping_page.select_ship_method()

    shipping_page.click_next()

    payment_page = Payment(browser)
    payment_page.wait_for_loading_spinner()
    payment_page.wait_for_page_to_load()

    assert 'checkout/#payment' in payment_page.browser.current_url

    # assert all the values entered at shipping are correctly saved at payment page
    ship_to_text = payment_page.ship_to_component_text()

    assert testdata["first_name"] in ship_to_text
    assert testdata["last_name"] in ship_to_text
    assert testdata["street_address"] in ship_to_text
    assert testdata["city"] in ship_to_text
    assert testdata["country"] in ship_to_text
    assert testdata["post_code"] in ship_to_text
    assert testdata["state"] in ship_to_text
    assert testdata["phone"] in ship_to_text

    payment_page.click_place_order()

    checkout_page = Checkout(browser)
    checkout_page.wait_for_page_to_load()

    assert 'checkout/onepage/success/' in checkout_page.browser.current_url

    # assert email and registration pops up
    assert testdata["email"] in checkout_page.contains(testdata["email"]).text
