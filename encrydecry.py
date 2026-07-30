#program to encrypt and decrypt
import random
import string

base = list(' '+string.ascii_letters+string.digits+string.punctuation)
key = list(' '+string.ascii_letters+string.digits+string.punctuation)
random.shuffle(key)

#encrypt the text
def encrypt():
  global secret
  global text
  text = input("What is your text")
  secret = ''
  x = 0
  for i in text:
    index = base.index(text[x])
    indexkey = key[index]
    secret += indexkey
    x +=1
  print(secret)
  text = ''

#Decrypt the encryption
def decrypt():
  global secret
  global text
  x = 0
  for i in secret:
    index = key.index(secret[x])
    indexbase = base[index]
    text += indexbase
    x +=1
  print(text)

y = input("1. Encrypting \n2. Decrypting\n type a number for its corresponding action")
while y == '1':
  encrypt()
  y = input("1. Encrypting \n2. Decrypting\n type a number for its corresponding action")
  while y == '2':
    decrypt()
    y = input("1. Encrypting \n2. Decrypting\n type a number for its corresponding action")

while y != '1' or y != '2':
  print("Thank you for using my program")
