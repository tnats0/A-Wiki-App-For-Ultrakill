from Tools.typeTools import *
from Tools.system_info import *
from Tools.time_info import *

# Rich 

from rich.console import Console
from rich.markup import escape 

myStyle:dict = {
    "success": "bold green",
    "error": "bold underline red",
    "important":"bold underline blue"
} 

terminal = Console()


cur_path = "C:\\Users\\TARIK ATASOY\\projects\\helloworld\\Projects\\Terminal\\Images\\ascii_image.txt"


def set_image(path=cur_path):

    with open(path,"r",encoding="utf-8") as image:

        part = image.readline()

        while part:
            print(part,end="")
            part = image.readline()


def imag_widht(path=cur_path):

    with open(path,"r") as file:

        line = file.readline()

        lenght = len(line)

        while line:

            line = file.readline()

            if len(line) > lenght:

                lenght = len(line)

    return lenght

distance  = imag_widht()+10

def sysStats():

    move(3,0)

    for x in info.values():

        typeMove(distance)
        terminal.print(f"• {escape(x)}",style="bold cyan")

def showDate():

    row = len(info.values())+6

    move(row,0)

    typeMove(distance)

    print(dateInfo,end="")

