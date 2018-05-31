# Import Modules:
from PIL import Image


# Define main:
def main():
    """The main function"""
    # # Open the image:
    # my_image = Image.open('flowers.jpg')
    #
    # # Display image size:
    # print(my_image.size)
    #
    # # Display image format:
    # print(my_image.format)
    #
    # # Display the image itself
    # # (uses default image viewer):
    # my_image.show()
    #
    # # Close the image:
    # my_image.close()

    ###############################

    # # Image Croping:
    #
    # # Define the area (x, y TO x , y):
    # area = (150, 200, 375, 600)
    #
    # # Open the image:
    # my_image = Image.open('bella.jpg')
    #
    # # Crop the image:
    # cropped_image = my_image.crop(area)
    #
    # # Show image:
    # cropped_image.show()
    #
    # # Close image:
    # my_image.close()

    ################################

    # Image Overlay:

    # Open the images:
    my_image = Image.open('me.jpg')
    ducky = Image.open('ducky.png')

    # Coordinates must match exactly:
    area = (350, 350, 500, 500)

    # Paste image on top of other:
    my_image.paste(ducky, area)

    # Show the result image:
    my_image.show()

    # Close both images:
    my_image.close()
    ducky.close()


# Call main:
main()
