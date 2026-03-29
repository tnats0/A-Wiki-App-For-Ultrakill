from pathlib import *
from customtkinter import *


MAIN_FOLDER = Path(__file__).absolute().parent

TESTAMENT_PATH = MAIN_FOLDER / "Testaments"
BOOK_PATH =  MAIN_FOLDER / "Books" 




def load_file(filePath:Path):

    with open(filePath,"r",encoding="utf-8") as file:

        data = file.read()

    return data

def load_folder(folderPath:Path):

    dataList = []
    
    files = folderPath.iterdir()

    for file in files:

        path = folderPath / file

        dataList.append(load_file(path))

    return dataList


testaments = load_folder(TESTAMENT_PATH)
books = load_folder(BOOK_PATH)
