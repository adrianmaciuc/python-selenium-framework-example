from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search')
    SEARCH_ICON_BTN = (By.CSS_SELECTOR, 'button.action.search')
    PRODUCT_ITEM_INFO = (By.CSS_SELECTOR, '.product-item-info')
    PROMO_PRODUCTS = (By.CSS_SELECTOR, '.blocks-promo a')
    FOOTER_LINKS = (By.CSS_SELECTOR, '.footer li a')
    NAVBAR_LINKS = (By.CSS_SELECTOR, '.navigation .level-top > a')

    def load(self):
        self.browser.get(self.URL)

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
        self.crawlable_link_check(*self.PROMO_PRODUCTS)

    def check_valid_links_of_footer(self):
        self.crawlable_link_check(*self.FOOTER_LINKS)

    def check_valid_links_of_navbar(self):
        self.crawlable_link_check(*self.NAVBAR_LINKS)
