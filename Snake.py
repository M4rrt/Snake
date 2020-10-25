import pygame, random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
pygame.init()
Screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')


c = 0

def game_restart():
    my_direction = LEFT
    snake = [(200, 200), (220, 200), (240, 200)]
    return my_direction, snake


def apples_pos():
    x = ((random.randint(0,290)//10)*20)
    y = ((random.randint(0,290)//10)*20)
    return (x, y)

def collission(c1 , c2):
    return ((c1[0] == c2[0]) and (c1[1] == c2[1]))

def snake_collission(snake):
    for i in range(1, len(snake)-1):
        if snake[0] == snake[i]:
            return True
    if (snake[0][0] <= -1 or snake[0][0] >= 600) or (snake[0][1] <= -1 or snake[0][1] >= 600):
        return True



snake = [(200, 200), (220, 200), (240, 200)]
snake_skin = pygame.Surface((20,20))
snake_skin.fill((100, 255, 100))

apples = (apples_pos())
apples_skin = pygame.Surface((20,20))
apples_skin.fill((255, 0, 0))

my_direction = LEFT
clock = pygame.time.Clock()
while True:

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_r:
                my_direction,snake = game_restart()

    if collission(snake[0], apples):
        #test if the snake head get
        apples = apples_pos()
        snake.append(apples)


    for i in range(len(snake)-1, 0, -1):
        # moves the others cells of the snake
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    
    if snake_collission(snake):
        c += 1
        print('losee', c)
        my_direction,snake = game_restart()

    Screen.fill((0, 0, 0))
    Screen.blit(apples_skin, apples)
    
    for pos in snake:
        Screen.blit(snake_skin,pos)

    pygame.display.update()