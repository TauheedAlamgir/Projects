# Milestone 3
# Tauheed Alamgir 101194927
# Diogo Reis Heitor 101201261

from Cimpl import *
from T093_image_filters import *

def check_command(command: str) -> bool:
    """
    """
    commands = ['L', 'S', '3', 'X', 'T', 'P', 'E', 'D', 'V', 'H', 'Q',]
    
    return command in commands

def run_commands(image_txt:str, command:str)->Image:
    check = check_command(command)
    if check == False:
        print("Non-existent command")
    else:
        image = copy(load_image(image_txt))
        
        if command == "S":
            filename = str(input("Enter filename: ")+".jpg")
            save_as(image, filename)
            
        elif command == '3':
            col1 = 'red'
            col2 = 'black'
            col3 = 'white'
            image = three_tone((image), col1, col2, col3)       
            
        elif command == "X":
            image = extreme_contrast(image)  
            
        elif command == "T":
            image = sepia(image) 
            
        elif command == "P":
            image = posterize(image) 
            
        elif command == "E":
            threshhold = 15
            image = detect_edges(image, threshhold) 
            
        elif command == "V":
            image = flip_vertical(image) 
            
        elif command == "H":
            image = flip_horizontal(image)
            
        else:
            print("No commands run")
    return image


def batch_file(filename:str):
    batch_file = open(filename)    
    line_number = 0
    position = 0
    
    command = [None]
    for line in batch_file:
        line_number +=1
    command = [None]*line_number
    batch_file.close()
    
    batch_file = open(filename)
    for line in batch_file:
        command[position] = line.split()
        position += 1
    batch_file.close()
    
    for i in range(0,len(command)):
        if len(command[i]) >= 2:
            for j in range(2,len(command[i])):
                
                result = run_commands(str(command[i][0]), str(command[i][j]))
                save_as(result,command[i][1])
                command[i][0] = command[i][1]
    check = load_image(str(command[i][1]))
    
batch_file("image_filter_batch.txt")
               
               
    