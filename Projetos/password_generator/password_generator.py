import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

lt = ''
letter_len = len(letters)
for letter in range(0, letter_len):
    r_letter = random.randint(0,letter_len)
    if nr_letters > letter:
        letter = letters[r_letter]
        lt = letter

print(lt)
#
# nn = ''
# num_len = len(numbers)
# for num in range(0, num_len):
#     num_len = random.randint(0 ,num_len)
#     if nr_numbers> num:
#         num = numbers[num_len]
#         nn = nn + num
#
# sy = ''
# sym_len = len(symbols)
# for sym in range(0, sym_len):
#     sym_len = random.randint(0 , sym_len)
#     if nr_symbols > sym:
#         sym = symbols[sym_len]
#         sy = sy + sym
#
# all_caracters = list(lt + nn + sy)
# random.shuffle(all_caracters)
#
# all = "".join(map(str, all_caracters))

# print(f'Your password is : {all}')

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P