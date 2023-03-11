import pygame
import time


pygame.init() #Инициализация библиотеки


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

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
font_style = pygame.font.SysFont(None, 50)

def message(msg, color): #Функция, которая будет показывать сообщения на экране
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
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
    if x1 >= dis_width or x1<0 or y1 >= dis_height or y1 < 0:
        game_over = True
    x1 += x1_change #Записываем новое значение положения змейки по оси х.
    y1 += y1_change #Записываем новое значение положения змейки по оси y.
    dis.fill(white)

    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(10)

message("Вы проиграли!", red)
pygame.display.update()
time.sleep(2)
pygame.quit() #Денициализация библиотеки
quit()