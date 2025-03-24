import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password = ""

password_length = int(nr_letters + nr_numbers + nr_symbols + 1)
print(password_length)

# Hard
password_list = []

for number in range(1, password_length):
    if nr_letters > 0:
        random_character = random.choice(letters)
        password_list.append(random_character)
        nr_letters -= 1
    elif nr_symbols > 0:
        random_symbol = random.choice(symbols)
        password_list.append(random_symbol)
        nr_symbols -= 1
    elif nr_numbers > 0:
        random_number = random.choice(numbers)
        password_list.append(random_number)
        nr_numbers -= 1

random.shuffle(password_list)

for number in range(0, len(password_list)):
    password = password + password_list[number]
print(password)
