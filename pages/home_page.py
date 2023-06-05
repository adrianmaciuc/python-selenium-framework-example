from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    URL = 'https://magento.softwaretestingboard.com/'
    SEARCH_INPUT = '#search'
    SEARCH_ICON_BTN = 'button.action.search'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        self.browser.maximize_window()

    def click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, by_locator))).click()

    def search_item(self, text):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.SEARCH_INPUT))).send_keys(text)
        self.browser.find_element(By.CSS_SELECTOR, self.SEARCH_ICON_BTN).click()
