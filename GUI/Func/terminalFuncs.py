from Data.system_info import *
from Data.time_info import *

from GUI.Func.typeTools import *
from GUI.gui_config import *



def set_image(path=IMAGE_PATH):

    with open(path,"r",encoding="utf-8") as image:

        part = image.readline()

        while part:
            print(part,end="")
            part = image.readline()


def imag_widht(path=IMAGE_PATH):

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

    for x in sys_info.values():

        typeMove(distance)
        terminal.print(f"• {x}",style="info",highlight=False)

def showDate():

    row = len(sys_info.values())+6

    move(row,0)

    typeMove(distance)

    print(dateInfo,end="")

