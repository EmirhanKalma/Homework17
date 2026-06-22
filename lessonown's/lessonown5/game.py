import pygame #Импортируем библиотеку БАЗА  ну как бы набор инструментов берем
import random #Импортируем рандом встроенная библиотека в python

pygame.init() #Запускает нашу игру

screen = pygame.display.set_mode((800, 600)) #Задаем базову длину и ширину экрана где будет воспроизведена игра в переменную screen

player_x = 50#Координата x игрока
player_y = 50#Координата y игрока
player_width = 50#Длина игрока
player_height = 50#Высота игрока

money_x = 250#Координата x монеты
money_y = 70#Координата y монеты
money_width = 20#Длина монеты
money_height = 20#Высота монеты

start_time = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 36)  # создаём шрифт, 36 — размер
speed = 5 #Контролирует скорость
clock = pygame.time.Clock() # Добавляем "таймер" для стабильной скорости
FPS = 60 #Количетсво FPS кадров каждую секунду
running = True #Создаем переменную running и указываем ей Правда чтобы когда пользователь нажимал крестик цикл закончился и закрылась окно с игрой
score = 0

game_over = False

while running: #Игра сама считается как бы бесконечным циклом
    for event in pygame.event.get(): #pygame.event.get() означает отслеживание клавиш и действий пользователя
      if event.type == pygame.QUIT:
         running = False
    time_left = pygame.time.get_ticks() - start_time
    keys = pygame.key.get_pressed() #Отслеживаем нажатие клавиш игрока
    
# Двигаемся влево, только если МЫ ЕЩЕ НЕ У КРАЯ (x > 0)
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
        
    # Двигаемся вправо, только если ПРАВЫЙ БОК не вылез за экран (x + ширина < 600)
    if keys[pygame.K_RIGHT] and player_x < 800 - player_width:
        player_x += speed

    # Сверху (y > 0)
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed

    # Снизу (y + высота < 400)
    if keys[pygame.K_DOWN] and player_y < 600 - player_height:
        player_y += speed
 
 
    screen.fill("purple") #Красит фон окна под заданный цвет , желательно ставить до объекта а то по просу закрасят объект
 
    player_react = pygame.Rect(player_x , player_y , player_width , player_height)
  
    # pygame.draw.rect(screen, ("black"), (player_x, player_y, player_width, player_height)) #pygame.draw.rect(screen , (color) , (x , y , width , height)) это готовая функция которая создает фигуру на холсте и мы специально сипользовали переменные чтобы их же потом и менять
    my_money = pygame.Rect(money_x, money_y, money_width, money_height) #Создает фигуру pygame.React(x , y , width , height)
    
    pygame.draw.rect(screen , ("yellow") , my_money) #Вырисовываем монетку
    pygame.draw.rect(screen , ("black") , player_react) #Вырисовываем игрока
    
    
    seconds_left = 30 - time_left // 1000
    text = font.render(f"Счёт: {score}", True, "white")  # рисуем текст
    second_time_left = font.render(f"Время осталось: {seconds_left}" , True , "white")
    screen.blit(text, (10, 10))  # показываем на экране в позиции x=10, y=10
    screen.blit(second_time_left , (10 , 40))
    
    if player_react.colliderect(my_money): #Смотрят касается ли хитбокс игрока хитбокса монеты и выдает Правда или Ложь
        print("Игрок каснулся монеты")
        random_x = random.randint(0 , 800)
        random_y = random.randint(0 , 600)
        money_x = random_x
        money_y = random_y
        score += 1
        print("Получнео 1 очко")
    pygame.display.flip() #Показываем готовый кадр игроку (переворачиваем холст)
    

    if time_left >= 30000:
        running = False
    # Это ограничение FPS (кадров в секунду)
    # Без него квадрат будет летать слишком быстро
    clock.tick(FPS)
    if running == False:
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
            screen.fill("black")
                    
            score_counted = font.render(f"Количетсов очков: {score}" , True , "white")
            screen.blit(score_counted , (250 , 250))
     
                    
              
         
            
            pygame.display.flip()
pygame.quit()