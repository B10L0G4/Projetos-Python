import os # limpar tela 
import random # numeros aleatorios  
from colorama import Fore, Back , Style  # para cores e estilos de fonte 

JogarNovamente= "s"
jogadas = 0
quemJoga = 2 #1 = CPU e 2 = Jogador 
maxJogadas = 9
vitoria = "n" #(or False)
velha = [
    [" "," "," "], 
    [" "," "," "],
    [" "," "," "]
]
def tela(): # para contruir e limpar a tela  
    global velha 
    global jogadas 
    os.system ("cls")
    print("    0   1   2")
    print("")
    print("0:  "+ velha [0][0] + " | " + velha [0][1] + " | " + velha [0][2])
    print("    -----------")
    print("1:  "+ velha [1][0] + " | " + velha [1][1] + " | " + velha [1][2])
    print("    -----------")
    print("2:  "+ velha [2][0] + " | " + velha [2][1] + " | " + velha [2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET) #antes estava jogadas // quemJoga = não funcionou quemjoga, mas diminuiu o numero de jogadas para  2

    
def JogadorJoga():
    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas
    
    if  quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Linha..."))
        c = int(input("Coluna..."))
        try:
            while velha[l][c] != " ":
                l = int(input("Linha..."))
                c = int(input("Coluna..."))
            velha[l][c]="X"
            quemJoga = 1 #mudança teste 
            jogadas = 1
        except:
            print("linha e/ou coluna inválida ")

def cpuJoga():
    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas
    
    if  quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,2)
        c = random.randrange(0,2)
        while velha[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c]="O"
        jogadas += 1
        quemJoga = 2


while True:
    tela()
    JogadorJoga()
    cpuJoga()
    #mm
    
    
    

    
    
    
 
 
