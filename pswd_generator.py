
import random

print("Welcome to our Password Generator")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','+']

nr_letters = int(input("How many letters you want in your password?\n"))
nr_numbers = int(input("How many numbers you want in your password?\n"))
nr_symbols = int(input("How many symbols you want in your password?\n"))

password_list = []

# adding letters
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# adding numbers
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# adding symbols
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# shuffle the list
random.shuffle(password_list)

# convert list into string
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
