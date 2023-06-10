from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time


class BasePage:
    LOADING_SPINNER = (By.CSS_SELECTOR, '[title="Loading..."]')

    def __init__(self, browser):
        self.browser = browser

    def get(self, *locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

    def get_multiple(self, *locator):
        return self.browser.find_elements(*locator)

    def click(self, *by_locator):
        self.get(*by_locator).click()

    def contains(self, text):
        return self.browser.find_element(By.XPATH, f'//*[contains(text(),"{text}")]')

    def wait_for_loading_spinner(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.LOADING_SPINNER))
        WebDriverWait(self.browser, 10).until_not(EC.presence_of_element_located(self.LOADING_SPINNER))

    def crawlable_link_check(self, *locator):
        # requests.head - HEAD requests are done when you do not need the content of the file, but only the status_code
        # or HTTP headers. We also need proper fake headers to not be blocked by the website.

        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

        for item in self.get_multiple(*locator):
            response = requests.head(item.get_attribute('href'), headers=headers)
            if response.status_code != 200:
                raise Exception(f'Link {item.get_attribute("href")} is broken')
            print(f'Link {item.get_attribute("href")} works fine')
            time.sleep(3.5)
