import requests
from utils.logger import get_logger

logger = get_logger()


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending GET request to: {url}")

        response = requests.get(url)

        logger.info(f"Response Status: {response.status_code}")
        return response
