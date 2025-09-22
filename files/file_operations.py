import shutil

def copy_file(src, dest):
    shutil.copy(src, dest)

def copy_folder(src, dest):
    shutil.copytree(src, dest)

def move_files(src, dest):
    shutil.move(src, dest)

if __name__ == "__main__":
    # Example usage
    # copy_file('./cleanup.py', './dest/cleanup.py')
    # copy_folder('.', './new_folder')
    # move_files("./list_directory.py", "./dest")
    move_files("./dest", "./destination")