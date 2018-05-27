"""Web Crawler Program"""


# Modules:
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# The main function gets a URL
# from the user and crawls the url:
def main():
    # Get URL from user::
    url = input("Enter a URL for the crawl: ")

    # Get BeautifulSoup Object:
    soup = get_soup(url)

    # Crawl url:
    crawl_url(url, soup)


def get_soup(url):
    # Get the source code:
    source_code = requests.get(url)

    # Convert to plain text:
    data = source_code.text

    # Convert to BeautifulSoup object:
    my_soup = BeautifulSoup(data, 'lxml')

    return my_soup


def crawl_url(url, soup):
    # For each anchor tag:
    for item in soup.findAll('a'):

        # Get the href value:
        href = urljoin(url, item.get('href'))

        # Get the text for the link:
        content = item.string

        # Display href and inner text:
        print(href)
        print(content)
        print("-----------")


# Call main:
main()
