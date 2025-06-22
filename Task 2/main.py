import random  # selcts random characters
import string  # provides a set of characters 
length = int(input("Enter length of password : "))  # asks user for input of password length 
characters = input("Enter characters to use (letters, numbers, symbols,all) : ") # asks user to input characters to use in password
if characters.lower() == "letters":  # checks if user input is letters
    characters = string.ascii_letters # provides letters 
elif characters == "numbers" :  # checks if user input is numbers
    characters = string.digits  # provides numbers
elif characters == "symbols": # checks if user input is symbols
    characters = string.punctuation # provides symbols
elif characters.lower() == "all":
    characters = string.ascii_letters + string.digits + string.punctuation # combines all characters 

else:
    print("Invalid input.please enter valid characters.")
    exit()  # exits the program is user input is invalid
password = ''.join(random.choice(characters) for x in range(length)) # generates a random password using the characters provided by user and length.
print(f"generated password is : {password}")


