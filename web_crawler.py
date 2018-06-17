"""Web Crawler Program"""


# Modules:
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Get and crawl url:
def main():
    """The main function"""

    # Get URL from user:
    url = input("Enter a URL for the crawl: ")

    # Get BeautifulSoup Object:
    soup = get_soup(url)

    # Crawl url:
    crawl_url(url, soup)


def get_soup(url):
    """Creates and returns BeautifulSoup object"""

    # Get the source code:
    source_code = requests.get(url)

    # Convert to plain text:
    data = source_code.text

    # Convert to BeautifulSoup object:
    my_soup = BeautifulSoup(data, 'lxml')

    return my_soup


def crawl_url(url, soup):
    """Crawls the url; displays anchor links and inner text"""

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
