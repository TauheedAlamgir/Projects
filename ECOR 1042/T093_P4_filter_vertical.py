# Diogo Reis Heitor 101201261 (filter)
# Tauheed Alamgir 101194927 (test)

from Cimpl import*
from unit_testing import check_equal

def flip_vertical(image: Image) -> Image:
    """
    Returns as image that has been flipped vertically, meaning it switches the top
    and the bottom of the image.
    >>> fliped_vertical(image)
    new_flipped_image
    
    """
    new_image = copy(image)
    image_width = get_width(image)
    image_height = get_height(image)
    
    for x in range(image_width):
        for y in range(image_height):
            color = get_color(image, x, y)
            set_color(new_image, x , image_height - 1 - y, color)
    return new_image

file = choose_file()
image = load_image(file)
show(flip_vertical(image))


def test_vertical() -> None:
    """
    Test function for our vertical flip function.
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
    >>> Checking pixel at (5, 0) PASSED)
    ------
    """
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(11, 11, 11)) 
    set_color(original, 1, 0,  create_color(12, 12, 12))
    set_color(original, 2, 0,  create_color(78, 34, 134)) 
    set_color(original, 3, 0,  create_color(61, 247, 154)) 
    set_color(original, 4, 0,  create_color(126, 126, 68)) 
    set_color(original, 5, 0,  create_color(252, 253, 254)) 

    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(11, 11, 11)) 
    set_color(expected, 1, 0,  create_color(12, 12, 12))
    set_color(expected, 2, 0,  create_color(78, 34, 134)) 
    set_color(expected, 3, 0,  create_color(61, 247, 154)) 
    set_color(expected, 4, 0,  create_color(126, 126, 68)) 
    set_color(expected, 5, 0,  create_color(252, 253, 254)) 
    
    vert = flip_vertical(original)
    for x, y, col in vert:
        check_equal('Checking pixel at (' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))
        
test_vertical()