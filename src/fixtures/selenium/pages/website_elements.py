from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging


class WebsiteElements:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def wait(self, method, selector):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of(self.driver.find_element(method, selector)))

    def accept_cookies(self):
        self.logger.info("Accept cookies")
        cookies = self.wait(By.XPATH, "//button[contains(text(),'Accept all')]")
        cookies.click()
