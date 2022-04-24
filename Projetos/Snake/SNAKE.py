import  pygame #importa a biblioteca do pygame - necessário instalar a bibliotéca (pip install pygame)
import random
from pygame.locals import*

UP = 0
RIGHT = 1 
DOWN = 2
LEFT = 3

pygame.init # necessário para iniciar o pygame 
screen = pygame.display.set_mode((600,600)) # set de tela 
pygame.display.set_caption("Snake")

snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10)) #para cada posição da snake
snake_skin.fill((255,255,255)) #define a cor da minha snake , rgb para branco 

apple_pos = (random.randint(0,590), random.randint(0,590)) # 590 valor máximo para não sair da tela 
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #fator rgb vermelho , cor da maçã

my_direction = LEFT  #COMEÇA INDO PARA ESQUERDA 

''' informações sobre jogos , nossa cobra será implementada com uma lista 
pois ela é uma lista de seguimento e cada seguimento será representada por uma tupla 
com valor de x e y onde será posicionada o quadrado. 
jogos são baseados em matrizes , nesse jogo nós implementamos uma 
matriz 600x600pixels. '''

while True: #todo jogo tem um laço infinito , com eventos de mudança , toque ou cliques
    for event in pygame.event.get(): # evento para fechamento do jogo 
        if event.type == QUIT:
            pygame.quit()
            
    if my_direction == UP:
        snake[0]
    screen.fill([0,0,0]) #limpa a tela 
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    
    pygame.display.update()