import  pygame #importa a biblioteca do pygame 
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


clock = pygame.time.Clock() #movimento da snake
while True: #todo jogo tem um laço infinito , com eventos de mudança , toque ou cliques
    clock.tick(20) #limitação de FPS , em 20FPS
    for event in pygame.event.get(): # evento para fechamento do jogo (1° evento )
        if event.type == QUIT:
            pygame.quit()
         
        if event.type ==KEYDOWN: #controle de movimentos , teclas  ( 2° evento)
           if event.key == K_UP:
                my_direction = UP
           if event.key == K_DOWN:
                my_direction = DOWN
           if event.key == K_LEFT:
                my_direction = LEFT
           if event.key == K_RIGHT:
                my_direction = RIGHT           
      
    if my_direction == UP: # movento direcional da cabeça 
        snake[0] = (snake[0][0],snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] +10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] -10,snake[0][1])
        
    for i in range(len(snake)-1,0-1):# laço para mover o corpo 
        snake[i] = (snake[i -1][0], snake[i-1][1])
        
    screen.fill([0,0,0]) #limpa a tela 
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    
    pygame.display.update()