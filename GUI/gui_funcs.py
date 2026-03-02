from GUI.Func.terminalFuncs import *


def get_input(msg:str):

    user_input = input(msg)

    return user_input

def handle_input(input):

    choices = ["1","2","3","4"]

    for x in choices:

        if x == input:
            return x

def create_layout():

    clear()

    sysStats()

    showDate()

    move(1,1)

    set_image()

    move(30,1) 


def menu():

    create_layout()

    msg = "Choose Action: "

    inp = get_input(msg)

    chc = handle_input(inp)


    