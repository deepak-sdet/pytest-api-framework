import pytest
from utils.api_helper import APIClient
from config.config import BASE_URL


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)
