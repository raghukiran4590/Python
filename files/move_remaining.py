import os, shutil

source_path = os.path.expanduser("~/Downloads/Cleanup_Backup/")
destination_path = os.path.expanduser("~/Downloads/Cleanup_Backup/Misc/")

for file in os.listdir(source_path):
    source_file_path = os.path.join(source_path, file)
    if not os.path.isdir(source_file_path):
        print("Not a Directory : "+file)
        destination_file_path = os.path.join(destination_path, file)
        shutil.move(source_file_path, destination_file_path)

print("File operation completed")