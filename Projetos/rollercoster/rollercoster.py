print(" Welcome to the Rollercoster! ")

height = float(input('Whats is your height in cm? '))

if height >= 120:
    print('You able to ride in the rollercoaster! Buy your ticket')
    bill = 0
    age = int(input('What is your age?  '))
    if age < 12 :
        bill = 7
        print(f'Your ticket is ${bill}')
    elif age < 17:
        bill = 12
        print(f'Your ticket is ${bill}')
    elif age > 17:
        bill = 18
        print(f'Your ticket is ${bill}')
    else:
        if age >= 45:
            bill = 0
            print(f'Your final bill is ${bill}')

    photo = input('Do you want a photo taken? Y or N  \n')
    photo = photo.upper()
    if photo == 'Y':
        bill = bill + 3
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')
else:
    print('You unable to ride! Sorry, you have to grow taller before you can ride. ')