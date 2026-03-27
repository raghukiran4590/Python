import base64

def encode_file_to_base64(file_path, destination_file_path=None):
    """
    Encodes a file into a base64 string.

    Args:
        file_path (str): The path to the file to encode.
        destination_file_path (str, optional): The path where the encoded file should be saved.

    Returns:
        str: The base64 encoded string.
    """
    try:
        # Open the file in read-binary mode ('rb')
        with open(file_path, 'rb') as file:
            # Read the file's binary content
            file_bytes = file.read()

        # Encode the bytes using base64.b64encode()
        encoded_bytes = base64.b64encode(file_bytes)

        # Convert the encoded bytes to a readable string (e.g., utf-8)
        encoded_string = encoded_bytes.decode('utf-8')

        with open(destination_file_path, "w") as output_file:
            output_file.write(encoded_string)

        print(f"File '{file_path}' has been encoded and saved to '{destination_file_path}'")

        return encoded_string

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_to_encode = 'dest.zip'
base64_output = encode_file_to_base64(file_to_encode, 'encoded_file.txt')