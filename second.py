import os
import hashlib
def compare_input_to_file(file_path, user_input):
    """Compares user input to the content of a text file.

    Args:
        file_path (str): The path to the text file.
        user_input (str): The user's input.

    Returns:
        bool: True if the input matches the file content, False otherwise.
    """

    with open(file_path, 'r') as file:
        file_content = file.read().strip()  # Remove leading/trailing whitespace

    return user_input == file_content

# Example usage:
file_path = "C:/hash/20speedy12/hash.txt"
user_password = input("Enter your password: ")
sha256_hash = hashlib.sha256()
sha256_hash.update(user_password.encode('utf-8'))
hasher = sha256_hash.hexdigest()

if compare_input_to_file(file_path, hasher):
    print("Correct, welcome, USER")
    #put log-on fuction here
else:
    print("Incorrect password.")