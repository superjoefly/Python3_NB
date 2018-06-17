"""Image Downloading Program"""

# The following program will download
# an image from the user specified url:

# Modules:
from urllib import request
from PIL import Image


# Gets url from user and downloads an image:
def main():
    """The main function"""

    # Get image url from user:
    image_url = input("Enter the url for the image to download: ")

    # Download the image:
    download_image(image_url)


# Downloads and verifies the image download:
def download_image(url):
    """Download and verify image"""

    # Define name for image:
    image_name = 'my_image.jpg'

    # Download the image:
    request.urlretrieve(url, image_name)

    # Validate image download:
    try:
        temp = Image.open(image_name)
        temp.close()
        print("Image downloaded successfully!")
    except IOError:
        print("There was an error! Please check the url for the image and try again!")


# Call main:
main()
