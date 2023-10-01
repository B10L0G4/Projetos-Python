import random

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")


position = input("Where do you want to put the treasure? ")
position2 = str(random.randint(0,2))

position = list(position)
position2 = list(position2)

linha =int(position[0])
coluna =int(position2[0])

linha = linha -1
coluna =coluna -1
map[coluna][linha] = " X"
print(f"{row1}\n{row2}\n{row3}")









