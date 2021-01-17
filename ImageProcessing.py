#
# ps7pr5.py  (Problem Set 7, Problem 5)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def grayscale(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that 
        creates and returns a new 2-D list of pixels for an image that is a 
        grayscale version of the original image.
    """ 
    all_grey = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(all_grey)):
        for c in range(len(all_grey[0])):
            grey = brightness(pixels[r][c])
            all_grey[r][c] = [grey, grey, grey]
    return all_grey

def fold_diag(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that 
        creates and returns a new 2-D list of pixels for an image in which 
        the original image is “folded” along its diagonal.
    """
    fold = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(fold)):
        for c in range(len(fold[0])):
            fold[r][c] = pixels[r][c]
            if r > c:
                fold[r][c] = [255,255,255]
    return fold

def mirror_horiz(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that 
        creates and returns a new 2-D list of pixels for an image in which 
        the original image is “mirrored” horizontally.
    """ 
    mid = len(pixels[0])//2
    mirror = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(mirror)):
        for c in range(len(mirror[0])):
            mirror[r][c] = pixels[r][c]
            if c >= mid:
                mirror[r][c] = pixels[r][mid-(c-mid)-1]
    return mirror

def extract(pixels, rmin, rmax, cmin, cmax):
    """ takes the 2-D list pixels containing pixels for an image, and that 
        creates and returns a new 2-D list that represents the portion 
        of the original image that is specified by the other four parameters. 
    """
    ex = blank_image(rmax-rmin, cmax-cmin)
    r1 = rmin
    for r in range(rmax-rmin):
        c1 = cmin
        for c in range(cmax-cmin):
            ex[r][c] = pixels[r1][c1]
            c1 = c1 + 1
        r1 = r1 + 1
    return ex        