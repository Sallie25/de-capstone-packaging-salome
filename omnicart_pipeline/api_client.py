import requests
import logging
from .config import ConfigManager

class ApiClient:
    """
    This class connects to an API and fetches data on products and users.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_products(self):

        response = requests.get(f'{self.base_url}/products/')
        if response.status_code == 200:
            logging.info('The server responded succefully!')
            products = response.json()
            return(products)
    
    def get_all_users(self):
        if response.status_code == 200:
            logging.info('The server responded succefully!')
            response = requests.get(f'{self.base_url}/users/')
            users = response.json()
            return(users)
    

def main():
    config = ConfigManager()

    client = ApiClient(config.base_url)

    # print(client.get_all_products())
    print(client.get_all_users())

if __name__ == "__main__":
    main()
    
