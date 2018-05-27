# Main Program
"""This is the main program"""

# Import Modules:
# import random
# import urllib.request
# from urllib import request

# import requests
# from bs4 import BeautifulSoup


import greetings

# Define main:
def main():
    """The main function for module examples"""

    # Call say_hello function of greetings module:
    greetings.say_hello()

    print("---------")

    # Call say_goodbye function of greetings module:
    greetings.say_goodbye()

    print("----------")


    ###########################





    ############################

    # # Web Crawler Example:
    # # Define url:
    # url = 'https://joefly.site/pages/projects/'
    # # Webcrawl the url:
    # web_crawl(url)


    ############################

    # # Exceptions
    # while True:
    #     try:
    #         # Convert value to integer:
    #         number = int(input("Enter a number: "))
    #         print(18 / number)
    #         # Break out of the loop:
    #         break
    #     # Handle value error:
    #     except ValueError:
    #         # Display a message:
    #         print("That's not a number! Try again...")
    #         print()
    #         # Continue to loop:
    #         # continue
    #     # Handle zero division error:
    #     except ZeroDivisionError:
    #         print("You cannot divide a number by zero!")
    #         print()
    #         # continue
    #     # Handle any error:
    #     except:
    #         print("Handling unknown error...")
    #         break
    #     # Display message no matter what:
    #     finally:
    #         print("I will display no matter what!")
    #         print()




    #############################
        # FUNCTIONS






# def web_crawl(url):
#
#     # Get the source code:
#     source_code = requests.get(url)
#     # Convert to plain text:
#     data = source_code.text
#     # Convert to BeautifulSoup object:
#     my_soup = BeautifulSoup(data, 'lxml')
#
#     # # Loop to find all icons with class of 'fa':
#     # for item in my_soup.findAll('i', {'class': 'fa'}):
#     #     title = item.decode_contents()
#     #     print(title)
#
#     # Loop to get all urls:
#     for item in my_soup.findAll('a', {'target':'_blank'}):
#         # Get the href value:
#         href = url + item.get('href')
#         # # Get the text for the link:
#         # title = item.string
#
#         # print(href)
#         # print(title)
#
#         #Get each item's data:
#         get_single_item_data(href)
#
#
#
# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     data = source_code.text
#     my_soup = BeautifulSoup(data, 'lxml')
#     for item in my_soup.findAll('h1'):
#         title = item.string
#         print(title)





# Call main
main()
