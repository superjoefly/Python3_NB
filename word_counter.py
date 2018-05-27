"""Word Count Program"""

# Import Modules:
import operator
import requests
from bs4 import BeautifulSoup

# Constants:
HEADING = ['WORD', 'COUNT']
DISPLAY = "{0:20s} {1:20s}"


def main():
    """Main Function"""

    # Get url to crawl:
    url = input("Enter a url to crawl: ")

    # Crawl url and return list of words:
    word_list = crawl(url)

    # Clean word list and return clean words:
    clean_words = clean_words_list(word_list)



    ###########################################
    # Display Table of Words and Count #

    # Create sorted dictionary (returns a list):
    sorted_list = create_dictionary(clean_words)

    # Display Table:
    display_table(sorted_list)
    ############################################




    # ###########################################
    # # Display Word Count for Specific Word #
    #
    # # Define search query:
    # search = input("Enter a word to search: ")
    #
    # display_search_count(search, clean_words)
    # ###########################################



# Crawls a url and returns a list of words:
def crawl(url):
    """Crawl url and return list of words"""

    source = requests.get(url).text
    data = BeautifulSoup(source, 'lxml')

    content = data.get_text()
    words = content.lower().split()

    return words


# Cleans the word list removing unwanted characters:
def clean_words_list(word_list):
    """Clean words of unwanted characters"""

    clean_words = []
    accepted = "abcdefghijklmnopqrstuvwxyz-'"
    for word in word_list:
        for i in list(word):
            if i not in list(accepted):
                word = word.replace(i, '')
        if len(word) > 0:
            clean_words.append(word)

    return clean_words


# Creates a sorted dictionary and returns a sorted list:
def create_dictionary(clean_words):
    """Create sorted dictionary and return list"""

    word_count = {}
    for word in clean_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort by key (alphabetically):
    sorted_dict = sorted(word_count.items(), key=operator.itemgetter(0))

    # # Sort by value (frequency):
    # sorted_dict = sorted(word_count.items(), key=operator.itemgetter(1))

    return sorted_dict


# Displays a table of words with word counts:
def display_table(sorted_list):
    """Display table"""

    # Display Formatted Table Headings:
    print("---------------------------")
    print(DISPLAY.format(HEADING[0], HEADING[1]))
    print("---------------------------")

    # Display Formatted Items:
    for item in sorted_list:
        print(DISPLAY.format(item[0], str(item[1])))


# Displays a word count search query:
def display_search_count(search, clean_words):
    """Display words and count"""

    count = 0
    for word in clean_words:
        if word == search:
            count += 1

    print("The word", search, "appears", count, "times.")


# Call main:
main()
