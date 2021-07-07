import logging
import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.env import BE, FE
from selenium.webdriver.chrome.options import Options


class Base:
    @pytest.fixture(autouse=True)
    def setup(self):
        if "cloud-api-dev.neuraldsp." in str(BE.url):
            options = Options()
            options.binary_location = os.environ['CHROME_BIN']
            options.add_argument("no-sandbox")  # FIXME: temporary workaround for https://github.com/SeleniumHQ/selenium/issues/4961#issuecomment-365251536
            options.add_argument("disable-dev-shm-usage")  # FIXME: temporary fix for https://stackoverflow.com/a/53970825
            options.add_argument("headless")
            options.add_argument("disable-application-cache")
            options.add_argument("window-size=1920,1080")
            self.logger = logging.getLogger(__name__)
            # self.driver = webdriver.Chrome(executable_path=os.environ['CHROME_DRIVER'], options=options) # USE: to run on remote machine
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) # USE: to run on local machine
            self.driver.get(FE.url)
            self.driver.get(FE.url)
            self.driver.implicitly_wait(5.0)
            self.driver.maximize_window()
            yield
            self.driver.close()

