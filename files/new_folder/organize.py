import os, shutil

# Declare Parent Folder Path
parent_folder_path = os.path.expanduser("~/Downloads/Cleanup_Backup/")
print(parent_folder_path)

# Create file types dictionary
file_types = {"Images": [".img", "jpeg", "jpg", "png", ".gif"],
             "Archive":[".zip", ".tar", ".gz", ".rar"],
             "Documents":[".txt", ".doc", "docx", ".pdf", ".json", ".xml", ".xlsx", ".csv"]}

# print(file_types)
# print(file_types.items())
# print(file_types.keys())
# print(file_types.values())

# Create subfolders
for folder_name in file_types:
    folder_path = os.path.join(parent_folder_path, folder_name)
    if not os.path.exists(folder_path):
        print(folder_name+" folder does not exist")
        os.makedirs(folder_path)
    else:
        print(folder_name+" folder does exist")
misc_folder_path = os.path.join(parent_folder_path, "Misc")
os.mkdir(misc_folder_path)


# Iterate thru parent folder path and move the files based on the extension
for file in os.listdir(parent_folder_path):
    print(file)
    file_path = os.path.join(parent_folder_path, file)
    if os.path.isfile(file_path):
        print("File found : "+file)
        for folder_name, extensions in file_types.items():
            for extension in extensions:
                if file.endswith(extension):
                    print("File extension found : "+extension)
                    destination_path = os.path.join(parent_folder_path, folder_name, file)
                    shutil.move(file_path, destination_path)
                else:
                    print("File extension not found : "+extension)
                    destination_path = os.path.join(parent_folder_path, "Misc", file)
                    shutil.move(file_path, destination_path)




