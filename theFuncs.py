from typeTools import *
import os
import ascii_magic as ascii

from system_info import *

cur_path = "C:\\Users\\TARIK ATASOY\\projects\\helloworld\\Projects\\Terminal\\ascii_image.txt"

imag_path = "C:\\Users\\TARIK ATASOY\\projects\\helloworld\\Projects\\Terminal\\ultrakill_logo(colored).webp"


def create_image(path=imag_path):
    pass


def set_image(path=cur_path):

    with open(path,"r",encoding="utf-8") as image:

        part = image.readline()

        while part:
            print(part,end="")
            part = image.readline()



def sysStats():

    column = 60

    for x in info.values():

        print(column*" ",x)



sysStats()
move(1,1)
set_image()