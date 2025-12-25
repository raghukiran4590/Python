
import os
import fnmatch
import shutil
from datetime import datetime
from pathlib import Path

def copy_last_modified_folder_contents() :

    """
    Finds the last modified folder in parent_directory and copies its contents
    to destination_directory.
    """
    parent_dir = "/Users/AF35861/Downloads/AWS"
    destination_dir = "/Users/AF35861/Downloads/AWS/AWS_Files"
    
    if not os.path.isdir(parent_dir):
        return f"{parent_dir} is not a valid parent dirtectory"

    subfolders = [
        os.path.join(parent_dir, folder)
        for folder in os.listdir(parent_dir)
        if os.path.isdir(os.path.join(parent_dir, folder)) and fnmatch.fnmatch(folder, "*-*")
    ]

    subfolders.sort(key=os.path.getmtime, reverse=True)
    
    if not subfolders:
        return None

    from_folder = subfolders[0]
    print(f"From Folder : {from_folder}")

    current_date = datetime.now()
    # print(current_date)

    formatted_date = current_date.strftime("%m-%d-%y")
    # print(formatted_date)

    to_folder = destination_dir + "_" + formatted_date
    print(f"To Folder : {to_folder}")

    if os.path.exists(to_folder):
        print(f"Destination folder '{to_folder}' already exists. Please remove it or choose a different destination.")
    else:
        try:
            shutil.copytree(from_folder, to_folder)
            print(f"Folder '{from_folder}' successfully copied to '{to_folder}'.")
        except FileNotFoundError:
            print(f"Error: Source folder '{from_folder}' not found.")
        except Exception as e:
            print(f"An error occurred during copying: {e}")
    
    for item_path in Path(to_folder).iterdir():
        if item_path.is_dir() and "east-1-json" in item_path.name:
            print(item_path)
            new_fld_name = "east-1-json_" + formatted_date
            shutil.copytree(os.path.join(to_folder, item_path.name), os.path.join(to_folder, new_fld_name))
            print(f"Folder '{item_path.name}' successfully copied to Folder {new_fld_name}.")
            shutil.rmtree(os.path.join(to_folder, item_path.name))
            print(f"Folder '{item_path.name}' successfully removed.")
        elif item_path.is_dir() and "east-2-json" in item_path.name:
            print(item_path)
            new_fld_name = "east-2-json_" + formatted_date
            shutil.copytree(os.path.join(to_folder, item_path.name), os.path.join(to_folder, new_fld_name))
            print(f"Folder '{item_path.name}' successfully copied to Folder {new_fld_name}.")
            shutil.rmtree(os.path.join(to_folder, item_path.name))
            print(f"Folder '{item_path.name}' successfully removed.")
        elif item_path.is_dir() and "east-1-csv" in item_path.name:
            # print(item_path)
            new_fld_name = "east-1-csv_" + formatted_date
            shutil.copytree(os.path.join(to_folder, item_path.name), os.path.join(to_folder, new_fld_name))
            print(f"Folder '{item_path.name}' successfully copied to Folder {new_fld_name}.")
            shutil.rmtree(os.path.join(to_folder, item_path.name))
            print(f"Folder '{item_path.name}' successfully removed.")
        elif item_path.is_dir() and "east-2-csv" in item_path.name:
            print(item_path)
            new_fld_name = "east-2-csv_" + formatted_date
            shutil.copytree(os.path.join(to_folder, item_path.name), os.path.join(to_folder, new_fld_name))
            print(f"Folder '{item_path.name}' successfully copied to Folder {new_fld_name}.")
            shutil.rmtree(os.path.join(to_folder, item_path.name))
            print(f"Folder '{item_path.name}' successfully removed.")
        else:
            print(f"Invalid Folder {item_path.name}")
    return to_folder

    

destination_folder = copy_last_modified_folder_contents()