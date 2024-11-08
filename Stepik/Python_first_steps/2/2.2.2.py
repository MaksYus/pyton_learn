import simplecrypt
from inspect import getsourcefile

print(getsourcefile(lambda:0))
      
passwords = []

with open("./2.2/passwords.txt",'r') as inp:
    passwords = [i.removesuffix('\n') for i in inp.readlines()]

print(passwords)

with open("./2.2/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    for password in passwords:
        try:
            print(simplecrypt.decrypt(password,encrypted))
            break
        except: pass