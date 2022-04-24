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
clock = pygame.time.Clock() #movimento da snake
while True: #todo jogo tem um laço infinito , com eventos de mudança , toque ou cliques
    clock.tick(20) #limitação de FPS , em 20FPS
    for event in pygame.event.get(): # evento para fechamento do jogo 
        if event.type == QUIT:
            pygame.quit()
    #posições para mover a cabeça da snake        
    if my_direction == UP: # movento direcional da snake, inicio baseadso na posição 0, 
#para cima Y diminui, para baixo aumenta, left e right iremos mexer no eixo X sendo esquerda diminui e direita aumenta 
        snake[0] = (snake[0][0],snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] +10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] -10,snake[0][1])
    for i in range(len(snake)-1,0-1):# laço para mover o corpo da snake, 
#cada posição do corpo da snake irá ocupar a posição do item anterior , iremos ocupar a posição -1 (posição anterior. )
        snake[i] = (snake[i -1][0], snake[i-1][1])
    screen.fill([0,0,0]) #limpa a tela 
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    
    pygame.display.update()