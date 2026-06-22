import pygame #Импортируем библиотеку БАЗА  ну как бы набор инструментов берем
import random #Импортируем рандом встроенная библиотека в python

pygame.init() #Запускает нашу игру

screen = pygame.display.set_mode((800, 600)) #Задаем базову длину и ширину экрана где будет воспроизведена игра в переменную screen
running = True #Создаем переменную running и указываем ей Правда чтобы когда пользователь нажимал крестик цикл закончился и закрылась окно с игрой
FPS = 10
clock = pygame.time.Clock() 

dx = 20  # двигаемся вправо на 20 пикселей
dy = 0 #двигаемя вверх или вниз

snake_width = 20
snake_height = 20
snake = [(400 , 300)]


apple_x = 400
apple_y = 300
apple_width = 20
apple_height = 20
# x, y = (400, 300) позволяет нам указывать что чему равняется
# теперь x = 400, y = 300
grew = False
game_over = False  
font = pygame.font.SysFont(None, 36) #Обязательно чтобы работали все другие шрифты и надписи
   
score = 0

while running: #Игра сама считается как бы бесконечным циклом
    for event in pygame.event.get(): #pygame.event.get() означает отслеживание клавиш и действий пользователя
      if event.type == pygame.QUIT:
         running = False
        

    

    
    keys = pygame.key.get_pressed() #Отслеживаем нажатие клавиш игрока 
         
    if keys[pygame.K_LEFT]:
        dx = -20
        dy = 0
        
    # Двигаемся вправо, только если ПРАВЫЙ БОК не вылез за экран (x + ширина < 600)
    if keys[pygame.K_RIGHT]:
        dx = 20
        dy = 0

    # Сверху (y > 0)
    if keys[pygame.K_UP]:
        dx = 0
        dy = -20

    # Снизу (y + высота < 400)
    if keys[pygame.K_DOWN]:
        dx = 0
        dy = 20
        
        
        
    screen.fill("green")
    
    x, y = snake[0]
    new_head = (x + dx, y + dy)
    snake.insert(0, new_head)
    
    for part in snake: #Тут воссоздали каждую чать змейки
      x, y = part #назначаем координату x и y
      my_snake = pygame.Rect(x , y , snake_width , snake_height)
      pygame.draw.rect(screen, "yellow", my_snake)
    
    my_apple = pygame.Rect(apple_x , apple_y , apple_width , apple_height)
    pygame.draw.rect(screen , ("red") , my_apple)
    
    if snake[0][0] <= 0 or snake[0][0] >= 800:
        running = False
    if snake[0][1] < 0 or snake[0][1] >= 600:
        running = False

    
    if snake[0] in snake[1:]:
        running = False

    text = font.render(f"Счет: {score}" , True , 'white')
    screen.blit(text , (10 , 10))
    
    head_rect = pygame.Rect(snake[0][0], snake[0][1], 20, 20)
    if head_rect.colliderect(my_apple):
        random_x = random.randint(0 , 39) * 20
        random_y = random.randint(0 , 30) * 20
        apple_x = random_x
        apple_y = random_y
        grew = True
        score += 1
        FPS += 1
    
    if grew:
      grew = False
    else:
      snake.pop()
    clock.tick(FPS) 
    if running == False:
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
            screen.fill("black")
                    
            score_counted = font.render(f"Количетсов очков: {score}" , True , "white")
            screen.blit(score_counted , (300 , 300))
            pygame.display.flip()

        
    
    
    pygame.display.flip() #Обязательная штука чтобы была видна сама картинка игры а так просто нечего не будет видно
