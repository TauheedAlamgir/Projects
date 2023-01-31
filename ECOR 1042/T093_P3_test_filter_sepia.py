from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color,create_image
from unit_testing import check_equal
from T093_P3_filter_sepia import sepia_tinting

def test_sepia() -> None:
    """
    A test function for sepia.
    
    >>> test_sepia()
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