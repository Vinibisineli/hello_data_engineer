from abc import ABC, abstractmethod
import requests
import logging

from requests.api import get

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class GetUserApi(ABC):

    def __init__(self, results: int) -> None:
        self.results = results
        self.base_url = f'https://randomuser.me/api/?results={self.results}'

    @abstractmethod
    def _get_endpoint(self, **kwargs) -> str:
        pass

    def get_user(self, **kwargs) -> dict:
        endpoint = self._get_endpoint(**kwargs)
        logger.info(f'Get user from: {endpoint}')
        user_data = requests.get(endpoint)
        user_data.raise_for_status()
        return user_data.json()


class UsersFrom(GetUserApi):

    def _get_endpoint(self, country: str) -> str:
        endpoint = f'{self.base_url}&nat={country}'
        return endpoint

print(UsersFrom(results=2).get_user(country="br"))