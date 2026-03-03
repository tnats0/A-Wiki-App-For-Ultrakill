from pathlib import *


TESTAMENT_PATH = Path(__file__).absolute().parent / "Testaments"

testamentList = list(TESTAMENT_PATH.iterdir())

testaments = {}


for i in range(len(testamentList)):

    with open(testamentList[i],"r") as file:

        testaments[f"{i+1}"] =  file.read()


