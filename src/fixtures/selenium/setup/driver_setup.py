import logging
import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.env.env import FrontendEnvironment
from selenium.webdriver.chrome.options import Options


class Setup:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = Options()
        # options.binary_location = os.environ['CHROME_BIN']  # set path of webdriver on Alpine image
        options.add_argument(
            "no-sandbox")  # FIXME: temporary workaround for https://github.com/SeleniumHQ/selenium/issues/4961#issuecomment-365251536
        options.add_argument("disable-dev-shm-usage")  # FIXME: temporary fix for https://stackoverflow.com/a/53970825
        options.add_argument("headless")
        options.add_argument("disable-application-cache")
        options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # USE: to run on local machine
        self.driver.get(FrontendEnvironment.base_url)
        self.driver.implicitly_wait(5.0)
        self.driver.maximize_window()
        yield
        self.driver.close()
