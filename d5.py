import random

print("Welcome to the Password Generator!")

letters_in = int(input("How many letters would you like in your password?"))
symbols_in = int(input("How many symbols would you like in your password?"))
numbers_in = int(input("How many numbers would you like in your password?"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ''
for char in range(1, letters_in+1):
    password += random.choice(letters)
for num in range(1, numbers_in+1):
    password += random.choice(numbers)
for symb in range(1, symbols_in+1):
    password += random.choice(symbols)


p_list = list(password)
random.shuffle(p_list)
p_final = ''
for char in p_list:
    p_final +=char
print(f"Your final password is: {p_final}")




