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
<<<<<<< HEAD
=======

#comment
>>>>>>> 42d3e4d4cdd90991265bdafa0c39fc3f9fda4efb
