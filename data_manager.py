import requests
from bs4 import BeautifulSoup


class DataManager:

    @staticmethod
    def scrape_website(url, date):
        return requests.get(f'{url}/{date}').text

    @staticmethod
    def get_content_from_website(website):
        return BeautifulSoup(website, 'html.parser')
