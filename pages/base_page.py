from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage:
    LOADING_SPINNER = (By.CSS_SELECTOR , '[title="Loading..."]')

    def __init__(self, browser):
        self.browser = browser

    def get(self, *locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

    def click(self, *by_locator):
        self.get(*by_locator).click()

    def wait_for_loading_spinner(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.LOADING_SPINNER))
        WebDriverWait(self.browser, 10).until_not(EC.presence_of_element_located(self.LOADING_SPINNER))

    def contains(self, text):
        return self.browser.find_element(By.XPATH, f'//*[contains(text(),"{text}")]') 