# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# letting the user choose the structure of hi/her password
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# creating a password array to hold the characters that will be extracted later
password = []

# creating a loop to in range of the user input amount(as max) and adding 1 as the last digit is not included
# later used the random.choice() function to get random letter and the range to iterate the process
for char in range(nr_letters + 1):
    password.append(random.choice(letters))

# creating a loop to in range of the user input amount(as max) and adding 1 as the last digit is not included
# later used the random.choice() function to get random letter and the range to iterate the process
for char in range(nr_symbols + 1):
    password.append(random.choice(symbols))

# creating a loop to in range of the user input amount(as max) and adding 1 as the last digit is not included
# later used the random.choice() function to get random letter and the range to iterate the process
for char in range(nr_numbers + 1):
    password.append(random.choice(numbers))

# Shuffle the final password list to randomize the position of the characters  used the random.shuffle() function
random.shuffle(password)

# Join the list to form a string using the join() function concatenated the password list as on string to ''
# this can be also done by char+=random.choice(numbers) inside th loops and using the password '' not a list
final_password = ''.join(password)

# passwords = ''
# for char in password:
#     passwords += char
# print(f"Your password is: {passwords}")

print(f"Your password is: {final_password}")

