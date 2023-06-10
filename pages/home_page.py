from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import requests
import time


class HomePage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search')
    SEARCH_ICON_BTN = (By.CSS_SELECTOR, 'button.action.search')
    PRODUCT_ITEM_INFO = (By.CSS_SELECTOR, '.product-item-info')
    PROMO_PRODUCTS = (By.CSS_SELECTOR, '.blocks-promo a')

    def load(self):
        self.browser.get(self.URL)
        self.browser.maximize_window()

    def get_list_of_product_items(self):
        return self.browser.find_elements(*self.PRODUCT_ITEM_INFO)

    def click_on_nth_product_item(self, number):
        product_items = self.get_list_of_product_items()
        product_items[number-1].click()

    def search_item(self, text):
        self.get(*self.SEARCH_INPUT).send_keys(text)
        self.browser.find_element(*self.SEARCH_ICON_BTN).click()

    def get_number_of_products(self):
        return len(self.get_multiple(*self.PROMO_PRODUCTS))

    def check_valid_links_of_products(self):
        for product in self.get_multiple(*self.PROMO_PRODUCTS):
            # HEAD requests are done when you do not need the content of the file, but only the status_code
            # or HTTP headers. We also need proper fake headers to not be blocked by the website.
            headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive"
                    }
            response = requests.head(product.get_attribute('href'), headers=headers)
            if response.status_code != 200:
                print(f'Link {product.get_attribute("href")} is broken')
            time.sleep(3)
