import os

def list_directory_files(path):
    for fn in os.listdir(path):
        print(fn)

list_directory_files('../basics')
    


