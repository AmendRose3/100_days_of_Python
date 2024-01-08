import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

letter_str = ""
num_str = ""
sym_str = ""

for i in range(nr_letters):
    letters_rand = random.choice(letters)
    letter_str += letters_rand

for i in range(nr_symbols):
    symbols_rand = random.choice(symbols)
    sym_str += symbols_rand

for i in range(nr_numbers):
    numbers_rand = random.choice(numbers)
    num_str += numbers_rand

# Combine the strings
partial_pass = letter_str + num_str + sym_str

# Convert the string to a list and shuffle it in-place
pass_list = list(partial_pass)
random.shuffle(pass_list)
print(pass_list)

# Join the shuffled list back into a string
new_password = ''.join(pass_list)

print(f"New Password is: {new_password}")
