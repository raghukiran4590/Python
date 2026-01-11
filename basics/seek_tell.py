with open("file.txt", 'r', encoding='utf-8') as f:
    # dwsljcfkn$dkjnfcvsldkjvn
    # Move the cursor to the 10th byte from the beginning
    f.seek(10)
    print(f"Cursor position after seek(10): {f.tell()}")

    # Read the next 5 bytes
    data = f.read(5)
    print(f"Data read: {data}")
    print(f"Cursor position after reading 5 bytes: {f.tell()}")

    # Move the cursor to 5 bytes before the end of the file
    # f.seek(-5, 2)
    # print(f"Cursor position after seek(-5, 2): {f.tell()}")

    # Read the last 5 bytes
    data = f.read(5)
    print(f"Data read: {data}")
    print(f"Cursor position after reading last 5 bytes: {f.tell()}")

with open("file2.txt", 'w') as f:
    f.write("Hello, World!")
    f.truncate(5)
    print(f"File truncated to 5 bytes.")
    print(f"Cursor position after truncation: {f.tell()}")
