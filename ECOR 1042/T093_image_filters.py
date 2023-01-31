# T093
# Dardell Duperval Numa 101173272 
# Tauheed Alamgir 101194927 
# Diogo Reis Heitor 101201261 
# Nabil Parham 101159258 

from Cimpl import*
import numpy
import string
import point_manipulation as pm

def choose_color(color: str) -> str:
    """
    Written By: Nabil Parham
    Each color is given it's r, g, b and there are many color options to choose
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)
    
    
    if color == 'black':
        return black

    elif color == 'white':
        return white

    elif color == 'red':
        return red

    elif color == 'lime':
        return lime

    elif color == 'blue':
        return blue

    elif color == 'yellow':
        return yellow

    elif color == 'cyan':
        return cyan

    elif color == 'magenta':
        return magenta

    elif color == 'gray':
        return gray
    
def three_tone(image: Image) -> Image:
    """
    Written By: Nabil Parham
    
    The function calculates the average of red, green, blue components of the images
    to determine its pixels brightness. If the average of the components brightness are from
    0 to 84 it sets to color1, same when the average components are between 85 to 170
    the color sets to color2, and finally the picture will set to color 3 after calculating the average of the components which are between 171 to 255 
    Nabil Parham
    """
    new_image = copy(image)
    
       
    color1 = input("Enter Color 1: ")
    color2 = input("Enter Color 2: ")
    color3 = input("Enter Color 3: ")
     
    for x, y, (r, g, b) in new_image:
        brightness = (r + g + b) / 3
        if brightness >= 0 and brightness <85:
            color_1 = choose_color(color1)
            set_color(new_image, x, y, color_1)
        elif brightness >= 85 and brightness < 171:
            color_2 = choose_color(color2)
            set_color(new_image, x, y, color_2)
        elif brightness >= 171 and brightness <= 255:
            color_3 = choose_color(color3)
            set_color(new_image, x, y, color_3)        
    return new_image

def posterize(image: Image) -> Image:
    """
    Written By: Tauheed Alamgir 
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

def extreme_contrast(image: Image)-> Image:
    """
    Written By: Diogo Reis Heitor
    This filter returns a copy of an image where all the pixels have 
    maximum contrast.
    """
    
    new_image = copy(image)
                     
    for pixel in image:
        x, y, (r, g, b) = pixel
        if r >= 0 and r <= 127:
            r = 0
        elif r >= 128 and r <= 255:
            r = 255
        if g >= 0 and g <= 127:
                g = 0
        elif g >= 128 and g <= 255:
                g = 255 
        if b >= 0 and b <= 127:
                b = 0
        elif b >= 128 and b <= 255:
                b = 255
        extreme_color = create_color(r, g, b)
        set_color(new_image, x, y,extreme_color)
    return new_image

def _adjust_component(value: int) -> int:
    """
    Written By: Tauheed Alamgir 
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

def sepia_tinting(image: Image) -> Image: 
    """
    Written By: Dardell Numa
    Takes an image's r,g,b sequence, converts it to grayscale using a rounded 
    avg. Following this, it upscales the red component and downscales the 
    blue component, thus resulting in an image that has a yellowish tint
    but retains the same brightness
    
    The percentage upscale and downscale depends on the range the r or b 
    component falls in.
    
    >>> r,g,b (78, 34, 134)
    (94, 82, 69)
    >>> r,g,b (126, 126, 68)
    (121, 106, 90)
    """
    new_image = copy(image)
    for x,y, (r,g,b) in image:
        if ((r+g+b)//3) < 63:
            sepia_tint = create_color(((r+g+b)//3)*1.1, (r+g+b)//3, ((r+g+b)//3)*0.9)
            set_color(new_image, x, y, sepia_tint)         
        if 63 <= ((r+g+b)//3) <= 191:
            sepia_tint = create_color(((r+g+b)//3)*1.15, (r+g+b)//3, ((r+g+b)//3)*0.85)
            set_color(new_image, x, y, sepia_tint)          
        if ((r+g+b)//3) > 191:
            sepia_tint = create_color(((r+g+b)//3)*1.08, (r+g+b)//3, ((r+g+b)//3)*0.93)
            set_color(new_image, x, y, sepia_tint)        
    return new_image        

def flip_horizontal(image: Image) -> Image:
    """
    Written by: Tauheed Alamgir
    
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
            set_color(new_image, width-x-1, y, create_color(r, g, b))
    return new_image

def flip_vertical(image: Image) -> Image:
    """
    Written by: Diogo Reis Heitor
    
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

def detect_edges(image : Image, threshold: int) -> Image:
    """
    Written by: Nabil Parham 
    This filter creates an image that looks like a pencil sketch, by changing the pixels' colours to black or white
    For every pixel that has a pixel below it, check the contrast between the two pixels: 
    1. If the contrast is high, change the top pixel's colour to black, but 
    2. If the contrast is low, change the top pixel's colour to white.
    """
    new_image = copy(image)
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    height = get_height(image)
    width = get_width(image)
    
    for y in range(height - 1):
        for x in range(width):
            (r, g, b) = get_color(image, x, y)
            (under_r, under_g, under_b) = get_color(image, x, y - 1)
            
            brightness1 = (r + g + b) //3
            brightness2 = (under_r + under_g + under_b) // 3
            value = abs(brightness1 - brightness2)

            if value > threshold:
                black= create_color(0,0,0)
                set_color(new_image,x,y,black)
            else:
                white = create_color(255,255,255)
                set_color(new_image,x,y,white)
    return new_image

#Draw Curve Script Begins Here

def _interpolation(lst: list) -> list:
    """
    Written By: Dardell Numa
    Takes list of tuples and returns the coefficient of its polynomial fit 
    function
    """
    lst = pm.sort_points(lst)
    lst = pm.get_x_y_lists(lst)
    for coordinates in lst:
        x,y = lst
    curve = numpy.polyfit(x, y, (len(x) - 1))
    return curve

def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> tuple:
    """
    Written By: Dardell Numa
    This function takes a max_x corresponding to the width of the image, a 
    coeff list received from _interpolation, and a val which depicts either 0
    or the image height to return a tuple containing where the function meets
    the top or bottom botder or 'nowhere' where there is no contact 
    within the parameters
    """
    
    epsilon = 0.1 #it was recommended to use a stepsize of 1, but this was
                  # was too large and always overshot the target value. 
    guess = 0.1
    func = 0
    
    n = len(polycoeff)
    i = 0
    while i in range(n):
        func += polycoeff[i]*guess**(n - 1 - i)
        i += 1  
    
    if n == 2:
        while (abs(func - val)) >= epsilon and (guess <= (max_x-1)):
            func = polycoeff[0]*guess + polycoeff[1]
            guess += epsilon    
            
    if n == 3:
        while (abs(func - val)) >= epsilon and (guess <= (max_x-1)):
            
            func = polycoeff[0]*guess**2 + polycoeff[1]*guess + polycoeff[2]
            
            guess += epsilon
            
    if n == 4:
        while (abs(func - val)) >= epsilon and (guess <= (max_x-1)):
            
            func = polycoeff[0]*guess**3 + polycoeff[1]*guess**2 \
            + polycoeff[2]*guess + polycoeff[3]
            
            guess += epsilon    
            
    if n == 5:
        while (abs(func - val)) >= epsilon and (guess <= (max_x-1)):
            
            func = polycoeff[0]*guess**4 + polycoeff[1]*guess**3 \
            + polycoeff[2]*guess**2 + polycoeff[3]*guess + polycoeff[4]
            
            guess += epsilon    

    if n == 6:
        while (abs(func - val)) >= epsilon and (guess <= (max_x-1)):
            
            func = polycoeff[0]*guess**5 + polycoeff[1]*guess**4 + \
            polycoeff[2]*guess**3 + polycoeff[3]*guess**2 + polycoeff[4]*guess \
            + polycoeff[5]
            
            guess += epsilon            
            
    if guess > (max_x - 1):
        return "nowhere"
    else:
        return (round(guess), val)
        
def _image_border_finding(image: Image, poly: list) -> list:
    """
    Written By: Dardell Numa
    This function uses polyval to find where the function received from 
    _interpolation meets the left or right border. Then it compiles this with 
    the results from _exhaustive_search to produce a list of tuples with 
    coordinates of where these intersection points are. 
    Finally, it returns a string of where these border crosses are and which
    borders are crossed
    """
    
    x_ = get_width(image)
    y_ =  get_height(image)
    
    
    top_border = _exhaustive_search((x_-1), poly, 0)
    bottom_border = _exhaustive_search((x_-1), poly, (y_-1))
    
    left = numpy.polyval(poly, 0)
    right = numpy.polyval(poly, x_)
    
    i=0
    while i in range(y_):
        if 0 <= numpy.polyval(poly, 0) <= (y_-1):
            left_border = (0, round(left))
        else:
            left_border = "nowhere"
        i+=1
        
    i = 0
    while i in range(y_-1):
        if 0 <= numpy.polyval(poly, x_) <= (y_-1):
            right_border = ((x_-1), round(right))
        else:
            right_border = "nowhere"   
        i+=1
        
    points = [top_border, bottom_border, left_border, right_border]
    
    print("There is a point ", str(points[0]), " at the top border of the image.")
    print("There is a point ", str(points[1]), " at the bottom border of the image.")
    print("There is a point ", str(points[2]), " at the left border of the image.")
    print("There is a point ", str(points[3]), " at the right border of the image.")
    
    return points



def draw_curve(image: Image):
    """
    Written By: Dardell Numa
    This function creates a set of 8 colors, then applies their r,g,b settings
    to a curve drawn from the function given by _interpolation. 
    This function also relies on user input, allowing the user to both choose
    the color and their point list
    
    The function works by first asking for number of data points. Following this, 
    it prompts the entry of the x values, then the entry of the y values.
    The x and y values are then organized in ascending order before being 
    added to a list where polyfit is used to generate a curve equation
    """  
    
    new_image = copy(image)
    
    n = int(input("Pick number of Elements between 2 and 6: ")) 
    
    pointx = list(map(int,input("\nEnter between 2-6 x numbers with no commas: ").strip().split()))[:n]
    pointy = list(map(int,input("\nEnter between 2-6 y numbers with no commas: ").strip().split()))[:n]
    
    pointx.sort
    pointy.sort
    
    points = [pointx, pointy]
    for coordinates in points:
        x,y = points
    curve = numpy.polyfit(x, y, (len(x) - 1)) 
    
    chosen_color = input("Choose your color: \n")
    if chosen_color == "black":
        chosen_color = create_color(0, 0, 0)
    if chosen_color == "white":
        chosen_color = create_color(255, 255, 255)
    if chosen_color == "blood":
        chosen_color = create_color(255, 0, 0)
    if chosen_color == "green":
        chosen_color = create_color(0, 255, 0)
    if chosen_color == "blue":
        chosen_color = create_color(0, 0, 255)
    if chosen_color == "lemon":
        chosen_color = create_color(255, 255, 0)
    if chosen_color == "aqua":
        chosen_color = create_color(0, 255, 255)
    if chosen_color == "pink":
        chosen_color = create_color(255, 0, 255)
    if chosen_color == "gray":
        chosen_color = create_color(128, 128, 128)       

    for x in range(get_width(image)):
        y = numpy.polyval(curve, x)
        if 0 <= y <= get_height(image):
            set_color(new_image, x,y, chosen_color)
                
    for x in range(get_width(image)):
        i = 0    
        for i in range(4):
            y = numpy.polyval(curve, x)
            y += 1
            i += 1
            if 0 <= y <= get_height(image):
                set_color(new_image, x,y, chosen_color)
     
    for x in range(get_width(image)):           
        i = 0
        for i in range(4):
            y = numpy.polyval(curve, x)
            y = y - 1
            i += 1
            if 0 <= y <= get_height(image):
                set_color(new_image, x,y, chosen_color)
    return new_image