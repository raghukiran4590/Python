import os
import fnmatch
import shutil
import subprocess

parent_dir = "/Users/AF35861/Downloads/AWS"
destination_dir = "/Users/AF35861/Downloads/AWS/AWS_Files"

subfolders = [
        os.path.join(parent_dir, folder)
        for folder in os.listdir(parent_dir)
        if os.path.isdir(os.path.join(parent_dir, folder)) and fnmatch.fnmatch(folder, "*-*")]

subfolders.sort(key=os.path.getmtime, reverse=True)
    
if not subfolders:
    print(f"subfolders is empty")

latest_folder = subfolders[0]
print(f"Latest Folder : {latest_folder}")

shutil.make_archive(latest_folder, 'zip', latest_folder)
print(f"Folder '{latest_folder}' successfully zipped to '{latest_folder}.zip'")

#-------------------------------- Email Sending part -----------------------

try:
    applescript_file_path = "email.applescript"
    attachment_path = f"{latest_folder}.zip"
    print(attachment_path)
    command = ["osascript", applescript_file_path, attachment_path]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print('Email sent successfully')
    if result.stderr:
            print("AppleScript errors:", result.stderr.strip())

except subprocess.CalledProcessError as e:
    print(f"Error executing AppleScript: {e}")
    print(f"Stderr: {e.stderr}")
except FileNotFoundError:
    print("Error: 'osascript' command not found. Ensure macOS is installed correctly.")
