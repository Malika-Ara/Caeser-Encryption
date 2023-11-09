import random
import string

char = " " + string.ascii_letters + string.digits + string.punctuation 
char = list(char)
key = char.copy()


random.shuffle(key)

#print(f"char : {char}")
#print(f"key : {key}")

plain_text = input("enter a message: ")
cipher_text = ""

for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]
    
print(f"Orignal message: {plain_text}")

print( f" Encrypted message: {cipher_text}")
