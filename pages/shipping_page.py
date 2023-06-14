from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class Shipping(BasePage):
    SHIP_METHOD_5 = (By.CSS_SELECTOR, 'input.radio')
    NEXT_BTN = (By.CSS_SELECTOR, '[data-role="opc-continue"]')
    COUNTRY_VALUE = (By.CSS_SELECTOR, '[name="country_id"]')
    STATE_VALUE = (By.CSS_SELECTOR, '[name="shippingAddress.region_id"] > div > select')

    def insert_text_in_input_field(self, text, field):
        input_fields = {
            "email": (By.CSS_SELECTOR, '#shipping #customer-email'),
            "first_name": (By.CSS_SELECTOR, '[name="firstname"]'),
            "last_name": (By.CSS_SELECTOR, '[name="lastname"]'),
            "street_address": (By.CSS_SELECTOR, '[name="street[0]"]'),
            "city": (By.CSS_SELECTOR, '[name="city"]'),
            "phone": (By.CSS_SELECTOR, '[name="telephone"]'),
            "post_code": (By.CSS_SELECTOR, '[name="postcode"]'),
        }

        self.get(*input_fields.get(field, "input field wrong or does not exist")).send_keys(text)

    def select_country(self, country):
        select = Select(self.get(*self.COUNTRY_VALUE))
        select.select_by_visible_text(country)

    def state_select(self, state):
        select = Select(self.get(*self.STATE_VALUE))
        select.select_by_visible_text(state)

    def select_ship_method(self):
        self.get(*self.SHIP_METHOD_5).click()

    def click_next(self):
        self.get(*self.NEXT_BTN).click()

    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.NEXT_BTN))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SHIP_METHOD_5))
