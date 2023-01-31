from T093_image_filters import *
from Cimpl import *

# DEFINITIONS


def execute_filter(command: tuple) -> Image:
    """
    """
    input_file, output_file, filters = command

    if filters == 'X':
        image = extreme_contrast((input_file))
        return image

    elif filters == 'T':
        image = sepia((input_file))
        return image

    elif filters == 'P':
        image = posterize((input_file))
        return image

    elif filters == 'V':
        image = flip_vertical((input_file))
        return image

    elif filters == 'H':
        image = flip_horizontal((input_file))
        return image

    elif filters == '3':
        col1 = 'yellow'
        col2 = 'magenta'
        col3 = 'cyan'
        image = three_tone((input_filename), col1, col2, col3)
        return image

    elif filters == 'E':
        image = detect_edges((input_filename), 10)
        return image


# SCRIPTING


file = input("Please input the name of the batch file: ")
batch_file = open(file, 'r')
i = 0
count = len(open(file).readlines())
newlist = [0] * count

for line in batch_file:
    newline = line.split()
    newlist[i] = tuple(newline)
    i += 1

for x in newlist:
    lenght = len(x)
    i = 2
    image = load_image(x[0])
    while i < lenght:
        image = execute_filter((image, x[1], x[i]))
        i += 1
    save_as(image, x[1])

batch_file.close()