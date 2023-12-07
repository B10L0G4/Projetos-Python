import time

from calculator.clearTerminal import clear_console

def add(n1,n2):
    return n1 + n2  

def sub(n1, n2):
    return n1 - n2 

def multi(n1, n2):
    return n1 * n2 

def div(n1, n2):
    return n1 / n2


calculator = {
    '+': add,
    '-': sub,
    '*': multi,
    '/': div
}

n1= int(input('Digite o primeiro numero\n'))
n2= int(input('Digite o segundo numero \n'))
for operacoes in calculator:
    print(operacoes)
operator= input("Qual operador vc deseja usar?\n")
   
if operator == '+':
    sum = calculator['+']
    resultado=sum(n1,n2)
    print(f'A soma de {n1} + {n2} é {resultado}')
    time.sleep(5) 
    clear_console()
elif operator == '-':
    subt = calculator['-']
    resultado=subt(n1,n2)
    print(f'A subtração de {n1} - {n2} é {resultado}')
    time.sleep(5) 
    clear_console()
elif operator == '*':
    mult = calculator['*']
    resultado=multi(n1,n2)
    print(f'A multiplicação de {n1} * {n2} é {resultado}')
    time.sleep(5) 
    clear_console()
else:
    divis = calculator['/']
    resultado=divis(n1,n2)
    print(f'A divisão de {n1} / {n2} é {resultado}')
    time.sleep(5) 
    clear_console()





