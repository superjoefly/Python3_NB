# Import Modules:
from PIL import Image
from PIL import ImageFilter


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











    # # Image Overlay:
    #
    # # Open the images:
    # my_image = Image.open('me.jpg')
    # ducky = Image.open('ducky.png')
    #
    # # Coordinates must match exactly:
    # area = (350, 350, 500, 500)
    #
    # # Paste image on top of other:
    # my_image.paste(ducky, area)
    #
    # # Show the result image:
    # my_image.show()
    #
    # # Close both images:
    # my_image.close()
    # ducky.close()

    ################################










    # # Working with Channels:
    #
    # # Open the images:
    # view_image = Image.open('view.jpg')
    # flowers_image = Image.open('flowers.jpg')
    #
    #
    # ##############################
    #
    #
    # # Display image mode:
    # # print(view_image.mode)
    #
    #
    # ##############################
    #
    #
    # # # Split into seperate channels:
    # # r, g, b = view_image.split()
    # #
    # # # Display seperate channels:
    # # r.show()
    # # g.show()
    # # b.show()
    #
    #
    # ##############################
    #
    #
    # # # Merge channels:
    # # r, g, b = view_image.split()
    # # merged_image = Image.merge("RGB", (r, g, b))
    # #
    # # # Merge in different order for effect:
    # # merged_image = Image.merge("RGB", (r, b, g))
    # # merged_image.show()
    #
    #
    # ###############################
    #
    #
    # # Merging two images:
    # # Separate Channels:
    # r1, g1, b1 = view_image.split()
    # r2, g2, b2 = flowers_image.split()
    #
    # # Merge channels:
    # merged_image = Image.merge("RGB", (r2, g1, b2))
    #
    # # Show the image:
    # merged_image.show()
    #
    # # Save the image:
    # merged_image.save('cool_image.jpg')
    #
    #
    #
    # # Close the images:
    # view_image.close()
    # flowers_image.close()

    ############################






    # # Transforms:
    #
    # my_image = Image.open('me.jpg')
    #
    # # # Resize:
    # # new_image = my_image.resize((500, 250))
    # # new_image.show()
    #
    # # # Flip:
    # # flipped_image = my_image.transpose(Image.FLIP_TOP_BOTTOM)
    # # flipped_image.show()
    #
    # # Spin:
    # spun_image = my_image.transpose(Image.ROTATE_90)
    # spun_image.show()
    #
    # # Close the image:
    # my_image.close()

    ############################








    # # Mode Conversion and ImageFilters:
    #
    # # Open the image:
    # my_image = Image.open('me.jpg')
    #
    # # # Convert to black and white:
    # # black_white = my_image.convert('L')
    # # black_white.show()
    #
    #
    # # # Blur image (ImageFilter):
    # # blurred = my_image.filter(ImageFilter.BLUR)
    # # blurred.show()
    #
    #
    # # # Detail image (ImageFilter):
    # # detailed = my_image.filter(ImageFilter.DETAIL)
    # # detailed.show()
    #
    #
    # # # Edges image (ImageFilter):
    # # edges = my_image.filter(ImageFilter.FIND_EDGES)
    # # edges.show()
    #
    #
    # # Close the image:
    # my_image.close()


# Call main:
main()
