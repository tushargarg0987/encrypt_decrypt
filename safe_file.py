import os
from cryptography.fernet import Fernet
import optparse

CRED = '\033[91m'
CEND = '\033[0m'

parser = optparse.OptionParser()

# setting required arguments list

parser.add_option("-i", "--input", dest="i_file", help=f"path of input file")
parser.add_option("-o", "--output", dest="o_file", help=f"path of output file")
parser.add_option("-k", "--key", dest="secret_key", help=f"secret key used for ")

(options, arguments) = parser.parse_args()

all_args = False

# Checking for function argument

if(len(arguments) > 0):
    function = arguments[0]

# Setting the values of arguments to variables

i_file = options.i_file
o_file = options.o_file
secret_key = options.secret_key

# Validating the arguments and giving relative errors

if(len(arguments) > 0 and i_file != None and o_file != None ):
    all_args = True
elif(len(arguments) == 0):
    print(CRED + "[-] Expected an argument encrypt or decrypt" + CEND)
elif(i_file == None):
    print(CRED + "[-] Expected an argument -i Input_File_Path" + CEND)
elif(o_file == None):
    print(CRED + "[-] Expected an argument -o Ouput_File_Path" + CEND)



if(all_args):
    if(function == "encrypt"):
        
        #encrytion
        
        key = Fernet.generate_key()
        with open(f"{o_file}/thekey.key","wb") as thekey:
            thekey.write(key)
        with open(i_file,"rb") as thefile:
            contents = thefile.read()
            ext = os.path.splitext(thefile.name)[1]
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(f"{o_file}/encrypted_file{ext}","wb") as thefile:
            thefile.write(contents_encrypted)

    elif(function == 'decrypt'):

        #decryption

        if(secret_key==None):
            print(CRED + "[-] Secret key is required for decryption, pass through -k" + CEND)
        else:
            with open(i_file,"rb") as thefile:
                contents = thefile.read()
                ext = os.path.splitext(thefile.name)[1]
            contents_decrypted = Fernet(secret_key).decrypt(contents)
            with open(f"{o_file}/decrypted_file{ext}","wb") as thefile:
                thefile.write(contents_decrypted)
    else:
        print(CRED + "[-] pass a valid argument encrypt or decrypt" + CEND)
