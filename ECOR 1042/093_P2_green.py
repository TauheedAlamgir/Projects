# Tauheed Alamgir 101194927 Group 093

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color,create_image
from unit_testing import check_equal

def green_channel(image: Image) -> Image:
    """
    This code takes a png image and applies a green filter on it and creates it 
    as a copy of the original image
    >>> image = load_image(choose_file())
    Choose the image you want to apply the filter to
    >>> green = green_channel(image)
    Uses the filter on the image but does not show the image
    >>> show(green)
    Opens the edited image in a new tab
    >>> show(image)
    Shows the original image in a new tab
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)
        set_color(new_image, x, y, green)
    return new_image
image = load_image(choose_file())
green = green_channel(image)
show(green)
show(image)

def test_green() -> None:
    """
    Tests a 6 pixel image within our green image if its pixels are green using 
    the expected and actual values
    >>> Checking pixel at (0, 0) PASSED
    ------
    >>> Checking pixel at (1, 0) PASSED
    ------
    >>> Checking pixel at (2, 0) PASSED
    ------
    >>> Checking pixel at (3, 0) PASSED
    ------
    >>> Checking pixel at (4, 0) PASSED
    ------
    >>> Checking pixel at (5, 0) PASSED
    ------
    """
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(23,45, 90))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(125, 250, 155))
    set_color(original, 3, 0,  create_color(80, 70, 60))
    set_color(original, 4, 0,  create_color(89, 199, 170))
    set_color(original, 5, 0,  create_color(2, 255, 246))    

    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 45, 0))
    set_color(expected, 1, 0,  create_color(0, 127, 0))
    set_color(expected, 2, 0,  create_color(0, 250, 0))
    set_color(expected, 3, 0,  create_color(0, 70, 0))
    set_color(expected, 4, 0,  create_color(0, 199, 0))
    set_color(expected, 5, 0,  create_color(0, 255, 0))    

    green = green_channel(original)
    for x, y, col in green:
        check_equal('Checking pixel at (' + str(x) + ', ' + str(y) + ')', col,
                      get_color(expected, x, y))
test_green()