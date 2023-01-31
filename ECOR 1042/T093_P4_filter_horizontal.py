# Tauheed Alamgir 101194927 Group 093 (filter)

from Cimpl import choose_file, load_image, create_color, set_color,\
                  show, Image, get_color, create_image, get_width, \
                  get_height, copy

def flip_horizontal(image: Image) -> Image:
    """
    Returns a horizontally flipped image by flipping it across the x-axis
    >>> pic = load_image(choose_file())
    Choose the picture to be flipped
    >>> show(flip_horizontal(pic))
    Shows the horizontally flipped image
    >>> show(pic)
    Shows the original image
    """
    new_image = copy(image)
    middlepixel = get_width(new_image) // 2
    width = get_width(new_image)
    height = get_height(new_image)
    for x in range(middlepixel):
        for y in range(height):
            r, g, b = get_color(image, x, y)
            r1, g1, b1 = get_color(image, abs(width - x) - 1, y)
            set_color(new_image, x, y, create_color(r1, g1, b1))
            set_color(new_image, width - x - 1, y, create_color(r, g, b))
    return new_image

pic = load_image(choose_file())
show(flip_horizontal(pic))
show(pic)
print("Have a great day!!!")