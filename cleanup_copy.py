import os

def delete_copy_files(folder_path):
    try:
        print(f"Deleting copy files...")
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                if '- Copy' in item:
                    os.remove(item_path)
                    print(f"Deleted: {item_path}")
            elif os.path.isdir(item_path):
                    if '- Copy' in item:
                        os.rmdir(item_path)
                        print(f"Deleted directory: {item_path}")
                    else:
                        print(f"Recursively checking inside directory: {item_path}")
                        delete_copy_files(item_path)
            else:
                print(f"Skipped: {item_path}")
    except PermissionError as pe:
        print(f"Permission error: {pe}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_copy_files("./")
    print(f"Copy files/folders deleted successfully.")