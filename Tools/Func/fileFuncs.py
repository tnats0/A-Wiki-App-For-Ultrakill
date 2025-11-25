import os

test_directory = "C:\\Users\\TARIK ATASOY\\Desktop\\test"

test_file = "C:\\Users\\TARIK ATASOY\\Desktop\\test\\metin.txt"

def find(directory):
    
    file = os.listdir(directory)

    return file

def delete(file):

    os.remove(file)

def info(file):

    sts = os.stat(file)

    sts_lst = {"Size":sts.st_size//1024,"Last Modified":sts.st_mtime,"Permissions":oct(sts.st_mode)}

    return sts_lst
    


