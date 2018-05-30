# Import Modules:
from PIL import Image


def main():
    # Open the image:
    my_image = Image.open('flowers.jpg')

    # Display image size:
    print(my_image.size)

    # Display image format:
    print(my_image.format)

    # Display the image itself
    # (uses default image viewer):
    my_image.show()



    my_image.close()


main()
