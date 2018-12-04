<<<<<<< HEAD
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
=======
from models.car import Car
def main():
    print ("hello world!")
    
<<<<<<< HEAD
>>>>>>> Development
=======
if __name__ == "__main__":
    main()
>>>>>>> c0d7b15e7a70629827288f211726fd51dc8dabd1
