# import info about system
from os import system, name 

# define function to clear screen 
def clearScreen(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux 
    else: 
        _ = system('clear') 

file = open("ascii car.txt", "r")
print(file.read())