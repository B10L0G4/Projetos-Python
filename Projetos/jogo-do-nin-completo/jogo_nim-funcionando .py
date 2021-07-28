def computador_escolhe_jogada(n,m):
    retirada = 1
    while retirada != m:
        if (n - retirada) %(m + 1) == 0:
            return retirada
        else:
            if retirada > m or retirada ==0 or m == 0:
                print ("jogada invalida")
            else:    
                retirada += 1
    return retirada
    
  
def usuario_escolhe_jogada(n,m):
    jogada = False
    while not jogada  :
        jogada_remove = int(input("Digite o numero de peças que deseja tirar: "))
        if jogada_remove > m or jogada_remove ==0 or m == 0:
            print ("jogada invalida")
            usuario_escolhe_jogada(n,m)
        else:
            jogada = True 
            
        return jogada_remove

def campeonato(): 
    print("**** Rodada 1 ****\n")
    partida()
    
    print("**** Rodada 2 ****\n")
    partida()
    
    print("**** Rodada 3 ****\n")
    partida()
    
    print("**** Final do campeonato!****\n")
    
    print("Placar: Você 0 X 3 Computador")    

def partida():
    n = int(input("Quantas peças?"))
    
    m = int(input("\nLimite de peças por jogada? \n"))
    if n < m or n==0 or m ==0:
        print ("Oops! jogada inválido! Tente de novo.")
        partida()
        
    computador_turno = False

    if n % (m +1) == 0:
 
        print("\n você começa\n")
    else:
        
        print ("\ncomputador começa")
        computador_turno = True
        
    while n > 0:
        if computador_turno:
            retirada = computador_escolhe_jogada(n,m)
            n = n - retirada
            if retirada == 1:
                print ('computador tirou 1 peças no tabuleiro \n')
                print("Agora resta ",n,"peças no tabuleiro \n")
            else:
                print('computador tirou',retirada,'do tabuleiro \n')
                print("Agora resta ",n,"peças no tabuleiro \n")

            computador_turno =False 
        else:
            jogada_remove = usuario_escolhe_jogada(n,m)
            n = n - jogada_remove
            if jogada_remove == 1:
                print("\nVocê tirou uma peça \n")
                print("Agora resta ",n,"peças no tabuleiro \n")
                computador_turno = True
            else:
                print("Restam ",jogada_remove,"peças no tabuleiro \n")
                print("Agora resta ",n,"peças no tabuleiro \n")
                computador_turno = True
        '''if n == 1:
            print ('Agora resta 1 peça no tabuleiro')
        else:
            print("Agora resta ",n,"peças no tabuleiro")'''
          
    print('Fim de Jogo \nComputador Ganhou')
def main():
    print ("Bem-vindo ao jogo do NIM! Escolha:\n" )
    a = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
    if a == 1:
        print(" \nVocê escolheu partida rápida \n")
        partida()
    elif a == 2:
        print("Voce escolheu um campeonato! \n")
        campeonato()
    else:
        print ("comando invalido , tente novamente ")
        main()            

main()

