import os, shutil
from pathlib import Path

def copy_file(src, dest):
    shutil.copy(src, dest)

def copy_folder(src, dest):
    shutil.copytree(src, dest)

def move_files(src, dest):
    shutil.move(src, dest)

def rename_file(src, dest):
    os.rename(src, dest)

def rename_files(src, dest):
    f = Path(src)
    f.rename(dest)


if __name__ == "__main__":
    # Example usage
    # copy_file('./cleanup.py', './dest/cleanup.py')
    # copy_folder('.', './new_folder')
    # move_files("./list_directory.py", "./dest")
    # move_files("./dest", "./destination")
    # rename_file('./destination/list_directory.py', './destination/renamed_list_directory.py')
    rename_files('./destination/renamed_list_directory.py','./destination/list_directory.py')