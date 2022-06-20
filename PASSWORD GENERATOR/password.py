import string
import random

# Declaration of a function that generates a random password of 8 characters every time it is run:

def generate_password():

        # Generating two random uppercase letters according to their ASCII code:
        char_1 = chr(random.randint(65, 90))
        char_2 = chr(random.randint(65, 90))

        # Generating two random lowercase letters according to their ASCII code:
        char_3 = chr(random.randint(97, 122))
        char_4 = chr(random.randint(97, 122))

        # Generating two random digits according to their ASCII code:
        char_5 = chr(random.randint(48, 57))
        char_6 = chr(random.randint(48, 57))

        # Generating two random printable non-alphanumeric characters for the password: 
        charlist = string.printable
        char_7 = charlist[random.randrange(62, 93)]
        char_8 = charlist[random.randrange(62, 93)]

        # Concatenating the characters into a string:
        password = char_1 + char_2 + char_3 + char_4 + char_5 + char_6 + char_7 + char_8
        # Converting the string to a list: 
        password2 = list(password)
        # Reordering the characters
        random.shuffle(password2)
        # Converting the list back to a string:
        result = "".join(password2)
        print(result)
        
# Calling the function:      
generate_password()

