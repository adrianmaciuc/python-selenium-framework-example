from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Checkout(BasePage):
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR , '.checkout-success a')
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR , '#registration a')
    REGISTRATION_COMPONENT = (By.CSS_SELECTOR , '#registration > div p')

    def registration_call_to_action_text(self):
        return self.get(*self.REGISTRATION_COMPONENT).text
    
    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.REGISTRATION_COMPONENT))




