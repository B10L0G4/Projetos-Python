

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
#
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

print('Welcome to the tip calculator! \n')

bill =float(input('What was the total bill? ')) # $124.56
tip = int(input('How much tip would you like to give? 10, 12, or 15? ')) #12
split = int(input('How many people to split the bill? ' )) #7

pay = bill / split
tip = round((tip / 100) * pay, 2)
pay = pay + tip

print(f'Each person should pay: {pay}')

# if tip == 10:
#     tip = 1.10
#     pay = (bill / split) * tip
#     print(f'Each person should pay: {pay}')
# elif tip == 12:
#     tip = 1.12
#     pay = (bill / split) * tip
#     print(f'Each person should pay: {pay}')
# else:
#     tip = 1.15
#     pay = round((bill / split) * tip, 2)
#     print(f'Each person should pay: {pay}')