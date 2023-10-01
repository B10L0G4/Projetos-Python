import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(type(names))

name = random.choice(names)
print(names)
print('choice',name)
print('choice',name[0])

random.shuffle(names)
print('shuffe',names)
print('shuffe',names[0])



# ['van', 'dante', 'ro', 'tati', 'mah']
# choice tati
# choice t
# shuffe ['ro', 'mah', 'van', 'dante', 'tati']
# shuffe ro

# van, dante, ro, tati, mah