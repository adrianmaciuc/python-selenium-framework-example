from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def get(self, locator):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable(locator))

    def click(self, by_locator):
        self.get(by_locator).click()
