from cryptography.fernet import Fernet
from pathlib import Path


base_dir = (Path(__file__)).parent
key_path = base_dir / "../db/key.txt"

with open(key_path,"r") as op :
    key = op.read().encode()

def encryption (data) :
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decryption (data) :
    f =Fernet(key)
    return f.decrypt(data.encode()).decode()


a = "hiiiii"
b = encryption(a)
print (b) 

print (decryption(b))