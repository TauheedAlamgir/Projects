# Dardell Duperval Numa 101173272 (filter)
# Tauheed Alamgir 101194927 Group 093 (test)

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color,create_image
from unit_testing import check_equal
# from T093_P3_filter_sepia import sepia_tinting

def sepia_tinting(image: Image) -> Image: 
    """
    Takes an image's r,g,b sequence, converts it to grayscale using an avg
    """
    new_image = copy(image)
    for x,y, (r,g,b) in image:
        if ((r+g+b)//3) < 63:
            black_white = create_color(((r+g+b)//3)*1.1, (r+g+b)//3, ((r+g+b)//3)*0.9)
            set_color(new_image, x, y, black_white)         
        if 63 < ((r+g+b)//3) < 191:
            black_white = create_color(((r+g+b)//3)*1.15, (r+g+b)//3, ((r+g+b)//3)*0.85)
            set_color(new_image, x, y, black_white)          
        if ((r+g+b)//3) > 191:
            black_white = create_color(((r+g+b)//3)*1.08, (r+g+b)//3, ((r+g+b)//3)*0.93)
            set_color(new_image, x, y, black_white)        
    return new_image        
    
#Main Script
file = choose_file()
image = load_image(file)
show(sepia_tinting(image))

def test_sepia() -> None:
    """
    Test funtion for our sepia filter
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
    """
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(11, 11, 11)) 
    set_color(original, 1, 0,  create_color(12, 12, 12))
    set_color(original, 2, 0,  create_color(78, 34, 134)) 
    set_color(original, 3, 0,  create_color(61, 247, 154)) 
    set_color(original, 4, 0,  create_color(126, 126, 68)) 
    set_color(original, 5, 0,  create_color(252, 253, 254)) 
     
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(12, 11, 9))
    set_color(expected, 1, 0,  create_color(13, 12, 10))
    set_color(expected, 2, 0,  create_color(94, 82, 69))
    set_color(expected, 3, 0,  create_color(177, 154, 130))  
    set_color(expected, 4, 0,  create_color(121, 106, 90))   
    set_color(expected, 5, 0,  create_color(255, 253, 235)) 
    
    sepia = sepia_tinting(original)
    for x, y, col in sepia:
        check_equal('Checking pixel at (' + str(x) + ', ' + str(y) + ')',
                col, get_color(expected, x, y))
test_sepia()