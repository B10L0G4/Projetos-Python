# Small Pizza: $15
#
# Medium Pizza: $20
#
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
#
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
size = size.upper()
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_pepperoni = add_pepperoni.upper()
extra_cheese = input("Do you want extra cheese? Y or N ")
extra_cheese = extra_cheese.upper()
bill = 0


if size == 'S':
    bill = 15
    print(bill)
else:
    if size == 'M':
        bill = 20
        print(bill)
    else:
        if size == 'L':
            bill = 25
            print(bill)
if add_pepperoni == 'Y':
    if size == "S":
        bill = bill + 2
        print(bill)
    else:
        bill =bill + 3
        print(bill)
if extra_cheese == 'Y':
    bill = bill + 1
    print(bill)


print(f'Your final bill is ${bill}')