# Tauheed Alamgir 101194927
# Diogo Reis Heitor 101201261

from Cimpl import *
from T093_image_filters import *
import numpy
import string
import point_manipulation as pm

# All the colors that can be used
Colors = ['black', 'white', 'red', 'lime', 'blue', 'yellow', 'cyan', 'magenta',
          'gray']
# All the image filters we have already created
ImageFilters = {'3': three_tone, 'X': extreme_contrast, 'F': sepia_tinting,
                'P': posterize, 'E': detect_edges, 'D': draw_curve,
                'V': flip_vertical, 'H': flip_horizontal}

def interactiveUI():
    """
    Prints the interactive section for the user to input data
    >>> Please select an option
    >>> L)oad Image  S)ave-as
    >>> 3)tone  X)treme Contrast  F)ilter Sepia  P)osterize
    >>> E)dge Detect  D)raw curve  V)ertical Flip  H)orizontal Flip
    >>> Q)uit
    """
    print('Please select an option')
    print('L)oad Image  S)ave-as')
    print('3)tone  X)treme Contrast  F)ilter Sepia  P)osterize')
    print('E)dge Detect  D)raw curve  V)ertical Flip  H)orizontal Flip')
    print('Q)uit')

# Takes users input and applies accordingly 
def search(x: str, picture: Image):
    """
    Returns the image with filter required from the compiled filter file
    """
    if x == 'X' or x == 'F' or x == 'P' or x == 'V' or x == 'H':
        image = ImageFilters[x](picture)
        show(image)
        return image
    elif x == '3':
        print('Please choose three colors')
        print(Colors)
        color1 = input(': ')
        color2 = input(': ')
        color3 = input(': ')
        image = ImageFilters[x](picture, color1, color2, color3)
        show(image)
        return image
    elif x == 'E' or x == 'D':
        print('Select a value/values between 2-6:')
        threshold = int(input(': '))
        image = ImageFilters[x](picture, threshold)
        show(image)
        return image
    return picture

Code = True
image = None
# If image = None then program checks if there is no image or no command
while Code == True:
    interactiveUI()
    letter = input(': ')
    letter = letter.upper()
    if letter == 'L':
        image = copy(load_image(choose_file()))
    if letter != 'L' and letter != 'S' and letter != 'Q':
        if image == None:
            if letter in ImageFilters.keys():
                print('No image loaded')
            else:
                print('No such command')
        elif letter not in ImageFilters.keys():
            print('No such command')
        else:
            image = search(letter, image)
            
    if letter == 'S': # Shows image first then lets you save it
        if image != None:
            show(image)
            print('File Name:')
            save_as(image)
            print("Have a Good Day!")
        else:
            print('Please select a image')
            
    if letter == 'Q': # Quits the program
        Code = False
        print("Have a Good Day!")
