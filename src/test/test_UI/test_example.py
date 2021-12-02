from fixtures.selenium.setup.driver_setup import Setup
from fixtures.selenium.pages.website_elements import WebsiteElements
"""Test Module class"""


class TestUIExample(Setup):
    """First test case"""

    def test_ui_case_one(self):
        web_elements = WebsiteElements(self.driver)
        web_elements.accept_cookies()
