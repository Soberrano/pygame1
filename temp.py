import pygame as pg
import random

#Настройка окна
WIDTH = 400
HEIGHT = 400
FPS = 60

#Настройка цвета
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

#Структура еды и персонажа
NEWFOOD = 40
FOODSIZE = 20
foodCounter = 0
playerSize = 50
x = 300
y = 100
player = pg.Rect(x,y,playerSize,playerSize)
foods = []

for i in range(20):
    foods.append(pg.Rect(random.randint(0, WIDTH - FOODSIZE)
                         ,random.randint(0,HEIGHT - FOODSIZE)
                         ,FOODSIZE
                         ,FOODSIZE))

#Движение
moving = 'STOP'
MOVESPEED = 10

#Инициализация
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False

        if i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                moving = 'LEFT'
            if i.key == pg.K_RIGHT:
                moving = 'RIGHT'
            if i.key == pg.K_UP:
                moving = 'UP'
            if i.key == pg.K_DOWN:
                moving = 'DOWN'

        if i.type == pg.KEYUP:
            if i.key == pg.K_LEFT or i.key == pg.K_RIGHT or i.key == pg.K_UP or i.key == pg.K_DOWN:
                moving = 'STOP'

        foodCounter += 1
        if foodCounter >= NEWFOOD:
            foodCounter = 0

        foods.append(pg.Rect(random.randint(0, WIDTH - FOODSIZE)
                             , random.randint(0, HEIGHT - FOODSIZE)
                             , FOODSIZE
                             , FOODSIZE))



    screen.fill(WHITE)

    if moving == 'DOWN' and player.bottom < HEIGHT:
        player.top += MOVESPEED
    if moving == 'UP' and player.top > 0:
        player.top -= MOVESPEED
    if moving == 'LEFT' and player.left > 0:
        player.left -= MOVESPEED
    if moving == 'RIGHT' and player.right < WIDTH:
        player.right += MOVESPEED


    #Отрисовка персонажа
    pg.draw.rect(screen, GREEN, player)

    #Удаление еды
    for food_col in foods:
        if player.colliderect(food_col):
            foods.remove(food_col)

    #Отрисовка еды
    for food in foods:
        pg.draw.rect(screen, RED, food)




    pg.display.update()
    clock.tick(FPS)
pg.quit()

























