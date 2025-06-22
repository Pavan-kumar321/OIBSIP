import random
import string
length = int(input("Enter length of password : "))
characters = input("Enter characters to use (letters, numbers, symbols) : ")
if characters.lower() == "letters":
    characters = string.letters
elif characters == "numbers" :
    characters = string.digits
elif characters == "symbols":
    characters = string.punctuation
else:
    characters = string.letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for x in range(length))
print(f"generated password is : {password}")
