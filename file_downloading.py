"""File Downloading Program"""


# The following program will download and verify
# a file from the user specified url:


# Modules:
from urllib import request


# Gets a url from the user and
# downloads the data from the url:
def main():
    """The main function"""

    # Get url from user:
    file_url = input("Enter url for file to download: ")

    # Download the file:
    download_file(file_url)


# Request data and write to file:
def download_file(url):
    """Request data and write to file"""

    # Request data from url:
    file_data = request.urlopen(url)

    # Get info about content:
    info = file_data.info()

    # Validate length of content:
    if info['content-length'] != None:
        write_file(file_data)
    else:
        print("No data present! Check the url and try again...")


# Create the file and write the data:
def write_file(file_data):
    # Read the data; convert to string:
    data = str(file_data.read())

    # Open file for write:
    in_file = open('data_file', 'w')

    # Write each line to file:
    for line in data:
        in_file.write(line)

    # Close file:
    in_file.close()


# Call main():
main()
