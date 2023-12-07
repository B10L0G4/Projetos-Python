import os
import platform

def clear_console():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system in ('Linux', 'Darwin'):
        os.system('clear')
    else:
        print("\n" * 100)

# # Testando a função
# teste = (input("Texto antes da limpeza do console."))
# teste1 = (input("Texto antes da limpeza do console."))
# print(teste,teste1)
# teste2 = (input("deseja continuart ."))
# print(teste2)

