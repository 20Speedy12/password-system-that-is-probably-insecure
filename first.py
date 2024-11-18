import os
import hashlib

print ("it is highly recommended that before you use this that you encrypt the hash via 'salt and pepper' or something else (stored at C:\hash\20speedy12) before you use this on something that is very important")
print ("if you don't have an encryption on the hash, I recommend that you bang your head on your keyboard a couple of times for your password and the result down somewhere")
print ("The hash is read-only so you would have to delete the hash to edit it")
user_input = input("Enter the password you want to use: ")
sha256_hash = hashlib.sha256()
sha256_hash.update(user_input.encode('utf-8'))
hashed_value = sha256_hash.hexdigest()

# Specify the directory path
directory_path = "C:/hash/20speedy12"

# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Write the hash to a file in the specified directory
file_path = os.path.join(directory_path, "hash.txt")
with open(file_path, 'w') as f:
    f.write(hashed_value)



def make_file_read_only(file_path):
    """Makes a file read-only.

    Args:
        file_path (str): The path to the file.
    """

    mode = 0o444  # Read-only permission for all users
    os.chmod(file_path, mode)

file_path = "C:/hash/20speedy12/hash.txt"
make_file_read_only(file_path)