import os # limpar tela 
import random # numeros aleatorios  
from colorama import Fore, Back , Style  # para cores e estilos de fonte 

JogarNovamente= "s"
jogadas = 9
quemJoga= 2 #1 = CPU e 2 = Jogador 
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
    print("Jogadas: " +   str(jogadas))
    
def JogadorJoga():
    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas
    
    if  quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Linha..."))
        c = int(input("Coluna..."))

        try:
            while velha[l][c] != "  ":
                l = int(input("Linha..."))
                c = int(input("Coluna..."))
            velha[l][c]="X"
            quemJoga = 1
            jogadas = 1
        except:
            print("linha e ou coluna invalida ")

def cpuJoga():
    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas
    
    if  quemJoga == 2 and jogadas < maxJogadas:
        l = randon.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != "  ":
            l = randon.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c]="O"
        quemJoga = 2
        jogadas += 1

while True:
    tela()
    JogadorJoga()
    cpuJoga()
    
    
    

    
    
    
 
 
