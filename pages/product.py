from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Product(BasePage):
    SIZE_S = (By.CSS_SELECTOR , '#option-label-size-143-item-167')
    SIZE_M = (By.CSS_SELECTOR , '#option-label-size-143-item-168')
    COLOR_ORANGE = (By.CSS_SELECTOR , '#option-label-color-93-item-56')
    COLOR_BLUE = (By.CSS_SELECTOR , '#option-label-color-93-item-50')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR , '#product-addtocart-button')
    ADD_TO_CART_SUCCESS_MSG = (By.CSS_SELECTOR , '[data-ui-id="message-success"]')

    def choose_size(self, size):
        if size.lower() == 's':
            self.get(*self.SIZE_S).click()
        elif size.lower() == 'm':
            self.get(*self.SIZE_M).click()
        else: 
            raise Exception("Test failed due to wrong or no size provided for product item")

    def choose_color(self, color):
        if color.lower() == 'blue':
            self.get(*self.COLOR_BLUE).click()
        elif color.lower() == 'orange':
            self.get(*self.COLOR_ORANGE).click()
        else: 
            raise Exception("Test failed due to wrong or no size provided for product item")
        
    def click_add_to_cart(self):
        self.get(*self.ADD_TO_CART_BTN).click()

    def add_to_cart_success_msg_visible(self):
        if self.get(self.ADD_TO_CART_SUCCESS_MSG):
            return True