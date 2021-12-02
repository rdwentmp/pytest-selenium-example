import requests
from fixtures.env.env import Environment

"""Test Module class"""


class TestAPIExample:
    """First test case"""

    def test_case_one(self):
        r = requests.get(Environment.base_url)
        assert r.status_code == 200
