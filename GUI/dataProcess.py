from pathlib import *

MAIN_FOLDER = Path(__file__).absolute().parent


TESTAMENT_PATH = MAIN_FOLDER / "Testaments"
BOOK_PATH =  MAIN_FOLDER / "Books" 


def load(lct:Path,encd:str="utf-8"):

    with open(lct,"r",encoding=encd) as file:

        data = file.read()

    return data


bookList = list(BOOK_PATH.iterdir())


books = [load(d) for d in bookList]




testamentList = list(TESTAMENT_PATH.iterdir())

testaments = {}

for i in range(len(testamentList)):

    with open(testamentList[i],"r") as file:

        testaments[f"{i+1}"] =  file.read()


print(books)
