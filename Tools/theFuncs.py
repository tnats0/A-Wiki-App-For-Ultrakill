from Tools.typeTools import *
from Tools.system_info import *

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


def sysStats():

    column = imag_widht() + 10

    move(3,0)

    for x in info.values():

        print(column*" ",x)

