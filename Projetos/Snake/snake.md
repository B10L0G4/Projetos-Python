### Quando inserir o import do PyGame não esquecer de instalar a bibliotéca (pip install pygame)

# Informações sobre o Jogo 

- Nossa snake será implementada como uma lista,pois ela é uma lista de seguimento e cada seguimento será representada por uma tupla com valor de x e y,
onde será posicionada no quadrado. 

- Jogos são baseados em matrizes , nesse jogo nós vamos implementamos uma matriz 600x600pixels. 
- Sobre o movento direcional da snake, inicia-se baseado na posição 0, 
    -Para cima em Y diminui, para baixo aumenta em Y, left e right iremos mexer no eixo X sendo esquerda diminui e direita aumenta

- No laço de repetição de movimento do corpo, cada posição do corpo da snake irá ocupar a posição anterior , iremos ocupar a posição -1 (posição anterior. )

