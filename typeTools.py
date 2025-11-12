# -- Modules -- #

import os
import sys
import time

from colorama import *

init(autoreset=True)

# -- Variables and Iterables -- #

colors:dict = {

"white":Fore.WHITE,
"blue": Fore.BLUE,
"green": Fore.GREEN,
"red": Fore.RED,
"yellow": Fore.YELLOW,
"magenta":Fore.MAGENTA,
"cyan": Fore.CYAN,
"lgreen": Fore.LIGHTGREEN_EX,
"lblue": Fore.LIGHTBLUE_EX,
"lred": Fore.LIGHTRED_EX,
"lblack": Fore.LIGHTBLACK_EX,
"lmagenta": Fore.LIGHTMAGENTA_EX,
"lcyan": Fore.LIGHTCYAN_EX

}


# -- Functions -- #

def type(text:str,delay:float=0.05,color:str="white",newline:bool=True)->None:  # Function to print with animation.

    for char in text:              # Loop through each character in the input text
        
        char = colors[color]+char  # Apply the specified color to the current character using the colors dictionary
        
        sys.stdout.write(char)     # Write the colored character to stdout without buffering
        
        sys.stdout.flush()         # Flush the output to ensure immediate display
        
        time.sleep(delay)          # Pause for the specified delay time between characters

    if newline: print()            # If newline is True, print a newline to move to the next line

def deleting(charNum:int)->None:    # Function to delete a specified number of characters from the console output
    
    sys.stdout.write(charNum*"\b")  # Move the cursor back by charNum positions using backspace characters
    sys.stdout.write(charNum*" ")   # Overwrite the characters with spaces to clear them from the display
    sys.stdout.write(charNum*"\b")  # Move the cursor back again to the original position after clearing
    sys.stdout.flush()              # Flush the output buffer to ensure the changes are displayed immediately

def clear()->None: # Function to clear the terminal
    
    if os.name == "nt":
        os.system("cls") # Windows
    else:
        os.system("clear") # Linux and Macos

#-- Test Side --#

def test()->None:

    for c in colors.keys():
        
        type("Hello World!",color=c,newline=False)
        print("  ",c)

