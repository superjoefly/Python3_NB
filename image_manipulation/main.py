"""Image Manipulation Examples"""

# Import Modules:
from PIL import Image
from PIL import ImageFilter



# Define main:
def main():
    """The main function"""

    # # Displaying image Info:

    # get_image_info()


    ##############################


    # # Cropping images:

    # crop_image()


    ##############################


    # # Overlaying images:

    # overlay_image()


    ##############################


    # # Working with Channels:

    # split_channels()

    # merge_channels()

    # merge_images()


    ##############################


    # # Transforms:

    # resize_image()

    # flip_image()

    # spin_image()


    ###############################


    # # Conversion and Filters:

    # bw_image()

    # blur_image()

    # sharpen_image()

    # find_edges()





# Getting Image Info:
def get_image_info():
    """Get mage Info"""

    # Open the image:
    my_image = Image.open('flowers.jpg')

    # Display image size:
    print(my_image.size)

    # Display image format:
    print(my_image.format)

    # Display image mode:
    print(my_image.mode)

    # Display the image itself (uses default image viewer):
    my_image.show()

    # Close the image:
    my_image.close()





# Cropping Images:
def crop_image():
    """Crop Image"""

    # Define the area (x, y TO x , y):
    area = (150, 200, 375, 600)

    # Open the image:
    my_image = Image.open('bella.jpg')

    # Crop the image:
    cropped_image = my_image.crop(area)

    # Show image:
    cropped_image.show()

    # Close image:
    my_image.close()





# Overlaying Images:
def overlay_image():
    """Overlay Image"""

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





# Working with Channels:

# Splitting Channels:
def split_channels():
    """Split Channels"""

    # Open the image:
    view_image = Image.open('view.jpg')

    # Split into seperate channels:
    r, g, b = view_image.split()

    # Display seperate channels:
    r.show()
    g.show()
    b.show()

    # Close the image:
    view_image.close()


# Merging Channels:
def merge_channels():
    """Merge Channels"""

    # Open the image:
    view_image = Image.open('view.jpg')

    # Merge channels:
    r, g, b = view_image.split()
    merged_image = Image.merge("RGB", (r, g, b))

    # Merge in different order for effect:
    merged_image = Image.merge("RGB", (r, b, g))
    merged_image.show()

    # Close the image:
    view_image.close()


# Merging Images:
def merge_images():
    """Merge Images"""

    # Open the images:
    view_image = Image.open('view.jpg')
    flowers_image = Image.open('flowers.jpg')

    # Separate Channels:
    r1, g1, b1 = view_image.split()
    r2, g2, b2 = flowers_image.split()

    # Merge channels:
    merged_image = Image.merge("RGB", (r2, g1, b2))

    # Show the image:
    merged_image.show()

    # Save the image:
    merged_image.save('cool_image.jpg')

    # Close the images:
    view_image.close()
    flowers_image.close()





# Transforms:
def resize_image():
    """Resize Image"""

    # Open the image:
    my_image = Image.open('me.jpg')

    # Resize:
    new_image = my_image.resize((500, 250))
    new_image.show()

    # Close the image:
    my_image.close()


def flip_image():
    """Flip Image"""

    # Open the image:
    my_image = Image.open('me.jpg')

    # Flip:
    flipped_image = my_image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_image.show()

    # Close the image:
    my_image.close()


def spin_image():
    """Spin Image"""

    # Open the image:
    my_image = Image.open('me.jpg')

    # Spin:
    spun_image = my_image.transpose(Image.ROTATE_90)
    spun_image.show()

    # Close the image:
    my_image.close()





# Conversions and Filters:
def bw_image():
    """Black and White Image"""

    # Open the image:
    my_image = Image.open('me.jpg')

    # Convert to black and white:
    black_white = my_image.convert('L')
    black_white.show()

    # Close the image:
    my_image.close()


def blur_image():
    """Blur Image"""

    # Open the image:
    my_image = Image.open('me.jpg')

    # Blur image (ImageFilter):
    blurred = my_image.filter(ImageFilter.BLUR)
    blurred.show()

    # Close the image:
    my_image.close()


def sharpen_image():
    """Sharpen Image"""

    # Open the image:
    my_image = Image.open('me.jpg')

    # Detail image (ImageFilter):
    detailed = my_image.filter(ImageFilter.DETAIL)
    detailed.show()

    # Close the image:
    my_image.close()


def find_edges():
    """Find Edges"""

    # Open the image:
    my_image = Image.open('me.jpg')

    # Edges image (ImageFilter):
    edges = my_image.filter(ImageFilter.FIND_EDGES)
    edges.show()

    # Close the image:
    my_image.close()



# Call main:
main()
