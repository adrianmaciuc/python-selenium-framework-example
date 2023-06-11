from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class ProductCatalog(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'
    FILTER_OPTIONS_XPATH = '//*[@class="filter-options-title"]'
    FILTER_SUBCATEGORY_OPTIONS_XPATH = '//div[@class="filter-options-content"]'
    PRODUCT_ITEM = (By.CSS_SELECTOR, '.product-item')
    FILTER_COMPONENT = (By.CSS_SELECTOR, '#layered-filter-block')
    FILTER_OPTIONS_CSS = '.filter-options-title'
    FILTER_SUBCATEGORY_OPTIONS_CSS = '.filter-options-content'

    def load(self, endpoint):
        self.browser.get(self.URL + endpoint)
        self.browser.maximize_window()

    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.PRODUCT_ITEM))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.FILTER_COMPONENT))
        time.sleep(1)

    def select_filter_option_by_text(self, text):
        self.contains(text).click()

    # def select_filter_subcategory_option_by_text(self, text):
    #     self.parent_contains(self.FILTER_SUBCATEGORY_OPTIONS_CSS, text).click()

    def get_number_of_products(self):
        return len(self.get_multiple(*self.PRODUCT_ITEM))
