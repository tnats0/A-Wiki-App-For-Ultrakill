from typeTools import *
import os
import ascii_magic

cur_path = "C:\\Users\\TARIK ATASOY\\projects\\helloworld\\Projects\\Terminal\\ascii_image.txt"

imag_path = 


def create_image()





def set_image(path=cur_path):

    with open(path,"r",encoding="utf-8") as image:

        part = image.readline()

        while part:
            print(part,end="")
            part = image.readline()


set_image()

