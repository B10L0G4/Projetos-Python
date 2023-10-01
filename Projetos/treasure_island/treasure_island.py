import sys

print(''' 
                                      _
                                     | |
                        __      _____| | ___ ___  _ __ ___   ___ 
                        \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ |
                         \ V  V /  __/ | (_| (_) | | | | | |  __/
                          \_/\_/ \___|_|\___\___/|_| |_| |_ \___|
                                         _        
                                        | |       
                                        | |_ ____ 
                                        | __/ _  \ 
                                        | || (_)  |
                                         \__\____/ 
            | |                                      (_)   | |               | |
            | |_ _ __ ___  __ _ ___ _   _ _ __ ___  ___ ___| | __ _ _ __   __| |
            | __| '__/ _ \/ _` / __| | | | '__/ _ \ | |/ __| |/ _` | '_ \ / _` |
            | |_| | |  __/ (_| \__ \ |_| | | |  __/ | |\__ \ | (_| | | | | (_| |
             \__|_|  \___|\__,_|___/\__,_|_|  \___  |_||___/_|\__,_|_| |_|\__,_|
                                                                                *
         _\/_ `O´       _\/_                 |                _\/_        _\/_ `O´
         /o\   |        /o\               |     |             /o\         /o\   |
          |    |         |                 .---.               |           |    |
        __|____|_________|_______     --  /     \  --     _____|___________|____|
                                 `~^~^~^~^~^~^~^~^~^~^~^~`
             
                            Your mission is to find the treasure.
''')

start = input('Do you want to start ? Y or N \n').upper()
if start == 'Y':
    side = input('Você tem dois caminhos, quer seguir pela direita ou esquerda?  ').lower()
    if side == 'direita':
        print('''Você foi pelo caminho da direita!\n Algum tempo caminhando, encontra uma
                                        |
                                       | |
                                      | _ |
                                     |.o '.|
                                     |'._.'|
                                     |     |
                                   ,'|  |  |`.
                                  |  |  |  |  |
                                  |,-'--|--'-.| KEY
        ''')
        space =input('Deseja embarcar na espaçonave e seguir para a lua ? Y or N ').upper()
        if  space == 'Y' :
            print('Game Over - Você esqueceu de vestir o traje espacial e morreu sufocado')
            sys.exit()
        else:
            print(f'Você decide pega o caminho da esquerda então!\nAlgum tempo caminhando, você se distrai,tropeça e cai num buraco.\n'
                  f'Por sorte não se machucou, mas acordou em um lugar desconhecido.\nVocê pode se aventurar ou buscar uma saída para a superficie.'
                  f'')
    else:
        print(f'Você decide pega o caminho da esquerda então!\nAlgum tempo caminhando, você se distrai,tropeça e cai num buraco.\n'
                  f'Por sorte não se machucou, mas acordou em um lugar desconhecido.\nVocê pode se aventurar ou buscar uma saída para a superficie.')
    ##################################################################################################################################################

    hole = input('Deseja explorar ou voltar a superficie ? E para explorar ou S para Subir \n').upper()
    if hole =='EXPLORAR' or hole == 'E':
        print('Na escuridão, você segue por uma caminho, chega em uma camara, iluminada por uma\n pouca luz vinda do alto,no centro do recinto há um ')
        print('''
                          .--------------------------------...
                       ,'-------------------------------,'   |
                      /                                /     |
                     /________________________________/    ,'|
                     |               ..               |  ,'  |
                     |___________-==/88\==-___________|,' /) |.
                     |  \    \     ((  ))     /    /  |  (/  |-. .
                     |   \    \     \{}/     /    /   |    .' .  .
                  . '|    \    \     )(     / _  /    |    ,   .  .
                 . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
               ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
                .  `    .     .       .  ,'\. ~-  . , .  .  .   .
                   .  `   .     ,   .      , ~~-.' .  .    .
                    DESEJA ABRIR ?
        ''')
        open = input('Y or N ').upper()
        if open == 'N':
            print('Você escolhe não se arriscar, isto é muito suspeito.\nQuando estava saindo para achar a saída, tropeçou mais uma vez e caiu em uma armadinha!\n'
                  'O baú se abre! ')
            print('''
                                E BUMMMMMMM!!!!!!!!!!!!!!!!!!!!!!!! 
                                           Você morreu! 
                                                )(
                                               /{}\
                                              (    )
                                 ,----------_____....----.--------,
                        _____.....-----~~~~~             |_______/ `
                       |       {}           {}           |      /  |
                       |        \  _---_  /              |     /
                       |         \/     \/                |   /   /
                        |         |() ()|                    | _/   /
                        |          \ + /                  |,'|~~
                       ,|         / HHH  \               ,'  |
                     ,'_|_______ /  \_/   \_____________:,' /) |.
                     |  \    \ {}          {}   /    /  |  (/  |_. .
                     |   \    \     {}       /    /   |    .' .  .
                  . '|    \    \            / _  /    |    ,   .  .
                 . . |\    \    \          _.( ~-.   /|\ ,' .   . .
               ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
                .  `    .     .       .  ,'\. ~-  . , .  .  .   .
                   .  `   .     ,   .      , ~~-.' .  .    .
            ''')
            sys.exit()
        else:
            print('''
                                            Quando você abre o baú 
                                         BUMMMMMMM!!!!!!!!!!!!!!!!!!!!!!!! 
                                                   Você morreu! 
                                                        )(
                                                       /{}\
                                                      (    )
                                         ,----------_____....----.--------,
                                _____.....-----~~~~~             |_______/ `
                               |       {}           {}           |      /  |
                               |        \  _---_  /              |     /
                               |         \/     \/                |   /   /
                                |         |() ()|                    | _/   /
                                |          \ + /                  |,'|~~
                               ,|         / HHH  \               ,'  |
                             ,'_|_______ /  \_/   \_____________:,' /) |.
                             |  \    \ {}          {}   /    /  |  (/  |_. .
                             |   \    \     {}       /    /   |    .' .  .
                          . '|    \    \            / _  /    |    ,   .  .
                         . . |\    \    \          _.( ~-.   /|\ ,' .   . .
                       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
                        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
                           .  `   .     ,   .      , ~~-.' .  .    .
            ''')
            sys.exit()

    if hole == 'S' or hole =='SUBIR':
        print('''Você olha para cima e vê uma luz, talvez a do buraco que caiu?\n'
              'Pouco a pouco você escala as paredes, mas não está no mesmo lugar, ao sair vê um 
              
                  .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
            DESEJA ABRIR ?
        ''')
    open1 = input('Y or N ').upper()
    if open1 == 'Y':
        print('''Vc abriu o Baú e encontrou ouro e riquesas! Parabéns vc venceu!
                                        /\
                                        )(
                                       /{}\
                                      (    )
                         ,----------_____....----.--------,
                _____.....-----~~~~~  /\          |_______/ `
               |    PARABÉNS         /  \        |      /  |
               |    PEGUE           /\/\/\       |     /
               |    SEU            /\ \/ /\       |   /   /
                |   LINDO         < <><><> >      | _/   /
                |   DIAMANTE       \/ /\ \/       |,'|~~
               ,|                    \  /        ,'  |
             ,'_|_____________________\/_______:,' /) |.
             |  \    \                /    /  |  (/  |_. .
             |   \    \     {}       /    /   |    .' .  .
          . '|    \    \            / _  /    |    ,   .  .
         . . |\    \    \          _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
    ''')
        sys.exit()
    else:
        print('FIM DE JOGO! \n Vc ficou com medo de um báu no meio da estrada achou que era mais uma armadilha '
                    'e perdeu seu prénio./\n'
                    'Está ilha foi completamente saqueada'
                    'Vá buscar riquezas em outro lugar! ')
else:
    print('Volte depois então! ')
