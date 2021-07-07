import os


class BE:
    url = os.environ.get('API_BASE_URL')


class FE:
    url = os.environ.get('BASE_URL')
