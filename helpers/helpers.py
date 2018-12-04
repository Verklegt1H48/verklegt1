#import info about system
from os import system, name

#define a function to clear the screen
def clearScreen():
    #windows
    if name == 'nt':
        _ = system('cls')
    #mac and linux
    else:
        _ = system('clear')
