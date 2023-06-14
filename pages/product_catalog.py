from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time


class ProductCatalog(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'
    FILTER_OPTIONS_XPATH = '//*[@class="filter-options-title"]'
    FILTER_SUBCATEGORY_OPTIONS_XPATH = '//div[@class="filter-options-content"]'
    PRODUCT_ITEM = (By.CSS_SELECTOR, '.product-item')
    FILTER_COMPONENT = (By.CSS_SELECTOR, '#layered-filter-block')
    FILTER_OPTIONS_CSS = '.filter-options-title'
    FILTER_OPTIONS_ITEMS = (By.CSS_SELECTOR, ".filter-options-item")
    FILTER_SUBCATEGORY_OPTIONS_CSS = (By.CSS_SELECTOR, ".filter-options-content > ol > li")
    PRICE_OF_PRODUCTS = (By.CSS_SELECTOR, '[data-price-type="finalPrice"]')
    SORTER_DROPDOWN = (By.CSS_SELECTOR, '#sorter')

    def load(self, endpoint):
        self.browser.get(self.URL + endpoint)
        self.browser.maximize_window()

    def get_selector_from_filter_options_by_text(self, text):
        return (By.XPATH, f'//*[@class="filter-options-content"]//*[contains(text(), "{text}")]')

    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.PRODUCT_ITEM))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.FILTER_COMPONENT))
        time.sleep(1)

    def filter_shopping_option_by(self, text):
        filter_option = self.find_element_by_text(self.browser.find_elements(*self.FILTER_OPTIONS_ITEMS), text)
        filter_option.click()

    def filter_subcategory_of_shopping_option_by(self, text):
        element = self.browser.find_element(*self.get_selector_from_filter_options_by_text(text))
        element.click()

    def get_number_of_products(self):
        return len(self.get_multiple(*self.PRODUCT_ITEM))

    def get_price_of_product_nth(self, nth):
        element = self.get_nth_of_elements(nth, *self.PRICE_OF_PRODUCTS)
        return element.text
    
    def sort_by(self, type):
        if type.lower() == 'price':
            select = Select(self.get(*self.SORTER_DROPDOWN))
            select.select_by_visible_text(type)
