import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
nome = input("Qual o seu nome? ")
linha = int(input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura: \n"))
coluna = random.randint(0,2)

player = f'{nome} escolheu {linha}'
computer = f'Computador escolheu {coluna}'

print(coluna)

if linha == 0:
    print(player, '\n', rock)
elif linha == 1:
    print(player, '\n',paper)
elif linha == 2:
    print(player, '\n',scissors)

if coluna == 0:
    print(computer, '\n',rock)
elif coluna == 1:
    print(computer, '\n',paper)
elif coluna == 2:
    print(computer, '\n',scissors)

if linha == coluna:
    print('Empate')
elif linha == 0 and coluna == 2:
    # pedra ganha tesoura
    print('You WIn')
elif linha == 0 and coluna == 1:
    # pedra perde papel
    print('Computer WIn')
elif linha == 1 and coluna == 0:
    # papel ganha pedra
    print('You WIn')
elif linha == 1 and coluna == 2:
    # papel perde tesoura
    print('Computer WIn')
elif linha == 2 and coluna == 1:
    # tesoura ganha papel
    print('You WIn')
elif linha == 2 and coluna == 0:
    # tesoura perde pedra
    print('Computer WIn')
