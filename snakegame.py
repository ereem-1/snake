import pygame
import time
import random


pygame.init() #Инициализация библиотеки


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dis_width = 800 #Ширина игрового поля
dis_height = 600 #Высота игрового поля
dis = pygame.display.set_mode((dis_width,dis_height)) #Задаем размер иигрового поля
#pygame.display.update()
pygame.display.set_caption('Snake from ereem')
game_over = False #Переменная, которая контролирует статус игры. False - значит игра продолжается
x1 = dis_width/2 #начальное значения положения змейки по оси х.
y1 = dis_height/2 #начальное значения положения змейки по оси у.
snake_block = 10 #Стандартаная величина сдвига змейки
x1_change = 0 #Перемнная, в которой будут записываться изменения положения змейки по оси х.
y1_change = 0 #Перемнная, в которой будут записываться изменения положения змейки по оси у.
clock = pygame.time.Clock()
snake_speeed = 15 #Скорость движения змейки
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font. render("Ваш счет: " + str(score), True, yellow)
    dis.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color): #Функция, которая будет показывать сообщения на экране
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = [] #создаем список, в котором будет храниться текущая длина змейки
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # Переменная, которая будет указывать расположение еды по оси х.
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # Переменная, которая будет указывать расположение еды по оси у.   
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Вы проиграли! Нажмите Q лдя выхода или C для повторной игры", red)
            pygame.display.update
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_c:
                       gameLoop()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_RIGHT:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_UP:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_DOWN:
                   y1_change = snake_block
                   x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_Head = [] #создаем список, в котором будет храниться показатель длины змейк при движениях
        snake_Head.append(x1) #Добавляем значения в список при изменении оси х.
        snake_Head.append(y1) #Добавляем значения в список при изменении оси y.
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0] # удаляем первый элемент в списке , чтобы она не увеличилась сама по себе при движениях
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)            
        #pygame.draw.rect(dis, black, [x1, y1, 10, 10])
        pygame.display.update()
        if x1 == foodx and y1 == foody: # Если координаты еды и координаты змейки совпадают, то еда появляется в новом месте
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speeed)
    pygame.quit() #Денициализация библиотеки
    quit()

gameLoop()    