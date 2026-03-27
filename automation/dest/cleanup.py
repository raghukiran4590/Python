import os

# Initialize Folder Paths
folder_original = "/Users/AF35861/Downloads/Cleanup"
folder_destination = "/Users/AF35861/Downloads/Cleanup_Backup"

# Make new Folder
os.mkdir(folder_destination)

#Iterate thru original Folder
for entry in os.scandir(folder_original):
    # Build Source and Destination File Paths
    location_original = os.path.join(folder_original,entry.name)
    location_destination = os.path.join(folder_destination,entry.name)
    
    # Move only if it is a file
    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)

print("File Operation Completed!")
