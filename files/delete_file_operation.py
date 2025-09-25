import os, shutil

def delete_file(fl):
    if os.path.isfile(fl):
        try:
            os.remove(fl)
        except OSError as e:
            print(f"Error : {fl} : {e.strerror}")
    else:
        print(f"Error : {fl} is not a valid file")

# delete_file("./destination/text.py")

