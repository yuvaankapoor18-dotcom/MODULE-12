import random


alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = alphabets.upper() 
numbers = "1234567890"

all_characters = alphabets + ALPHABETS + numbers

password_length = 12

PASSWORD = "".join(random.choices(all_characters, k=password_length))

print(PASSWORD)
