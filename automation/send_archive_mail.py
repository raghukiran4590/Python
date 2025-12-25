import subprocess
import os
import glob

try:
    directory_path = "/Users/AF35861/Downloads/AWS"
    zip_files = glob.glob(os.path.join(directory_path, "*.zip"))
    if not zip_files:
        print("No zip files found in the directory.")
        exit(1)
    latest_zip_file = max(zip_files, key=os.path.getmtime) 
    print(f"Latest zip file: {latest_zip_file}")

    applescript_file_path = "email.applescript"
    # attachment_path = "/Users/AF35861/Downloads/AWS/AWS_Files_11-03-25.zip"
    # print(attachment_path)
    command = ["osascript", applescript_file_path, latest_zip_file]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print('Email sent successfully')
    if result.stderr:
            print("AppleScript errors:", result.stderr.strip())

except subprocess.CalledProcessError as e:
    print(f"Error executing AppleScript: {e}")
    print(f"Stderr: {e.stderr}")
except FileNotFoundError:
    print("Error: 'osascript' command not found. Ensure macOS is installed correctly.")
