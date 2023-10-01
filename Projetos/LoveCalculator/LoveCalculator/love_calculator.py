print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name1 = name1 + name2

love1 = name1.count('l'),name1.count('o'),name1.count('v'),name1.count('e')
true1 = name1.count('t'),name1.count('r'),name1.count('u'),name1.count('e')

l = sum(i for i in love1)
t = sum(i for i in true1)
#
love =str(t) + str(l)
love = int(love)

if love < 10 or love > 89:
    print(f'Your score is {love}, you go together like coke and mentos.')
elif 41 < love < 51:
    print(f'Your score is {love}, you are alright together.')
else:
    print(f'Your score is {love}.')


