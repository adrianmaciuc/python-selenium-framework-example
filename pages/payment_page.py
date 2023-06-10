from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class Payment(BasePage):
    PLACE_ORDER_BTN = (By.CSS_SELECTOR , '[title="Place Order"]')
    SHIP_TO = (By.CSS_SELECTOR , '.ship-to .shipping-information-content')

    def ship_to_component_text(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SHIP_TO))
        return self.get(*self.SHIP_TO).text

    def click_place_order(self):
        self.get(*self.PLACE_ORDER_BTN).click()

    def wait_for_page_to_load(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.PLACE_ORDER_BTN))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SHIP_TO))