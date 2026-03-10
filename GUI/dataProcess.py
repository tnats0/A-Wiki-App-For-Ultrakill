from pathlib import *

MAIN_FOLDER = Path(__file__).absolute().parent


TESTAMENT_PATH = MAIN_FOLDER / "Testaments"
BOOK_PATH =  MAIN_FOLDER / "Books" / "book1_4.txt"



with open(BOOK_PATH,"r",encoding="utf-8") as book:
    
    bookData_1_4 = book.read()



testamentList = list(TESTAMENT_PATH.iterdir())

testaments = {}

for i in range(len(testamentList)):

    with open(testamentList[i],"r") as file:

        testaments[f"{i+1}"] =  file.read()


