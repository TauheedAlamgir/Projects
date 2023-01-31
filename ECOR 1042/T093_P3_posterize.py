# Tauheed Alamgir 101194927 Group 093

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, _adjust_component 

def posterize(image: Image) -> Image:
    """
    Returns a copy of the original but reducing the amount of colors in it
    >>> pic = load_image(choose_file())
    Choose the picture to be edited
    >>> show(posterize(pic))
    Shows the posterized image
    >>> show(pic)
    Shows the original image
    """
    new_image = copy(image)
    for pixe1 in image:
        x, y, (r, g, b) = pixe1
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        new_colour = create_color(r, g, b)
        set_color(new_image, x, y, new_colour)
    return new_image

def _adjust_component(value: int) -> int:
    """
    Returns the quadrant in which the component lies and returns the
    midpoint value of that quadrant and there can only be four midpoints for the
    four quadrants: 31,95,159 or 223
    >>> print(_adjust_component(2))
    31
    """
    if value >= 0 and value <= 63:
        return 31
    elif value > 63 and value <= 127:
        return 95
    elif value > 127 and value <= 191:
        return 159
    elif value > 191 and value <= 255:
        return 223

pic = load_image(choose_file())
print(_adjust_component(129)) # You can try any value between 0-255
show(posterize(pic))
show(pic)