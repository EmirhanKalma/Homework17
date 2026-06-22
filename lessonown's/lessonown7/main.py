





import pygame #Импортируем библиотеку БАЗА  ну как бы набор инструментов берем

pygame.init() #Запускает нашу игру

screen = pygame.display.set_mode((800, 600)) #Задаем базову длину и ширину экрана где будет воспроизведена игра в переменную screen
running = True #Создаем переменную running и указываем ей Правда чтобы когда пользователь нажимал крестик цикл закончился и закрылась окно с игрой
menu = True
FPS = 60
clock = pygame.time.Clock() 

roket_x = 20
roket_y = 260
roket_width = 10
roket_height = 80

roket_ai_x = 770
roket_ai_y = 260
roket_ai_width = 10
roket_ai_height = 80

ball_x = 400
ball_y = 300
ball_width = 20
ball_height = 20
ball_dx = 4  # скорость по x
ball_dy = 4  # скорость по y

ai_score = 0
my_score = 0

roket_speed = 5
ai_roket_speed = 5
# x, y = (400, 300) позволяет нам указывать что чему равняется
# теперь x = 400, y = 300

font = pygame.font.SysFont(None, 36) #Обязательно чтобы работали все другие шрифты и надписи
score = 0





    
    
    

  
  
while running: #Игра сама считается как бы бесконечным циклом
    for event in pygame.event.get(): #pygame.event.get() означает отслеживание клавиш и действий пользователя
      if event.type == pygame.QUIT:
         running = False
    screen.fill(str("black"))
    
    
    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= 600 - ball_height:
      ball_dy = -ball_dy

    
    
    
    
    keys = pygame.key.get_pressed() #Отслеживаем нажатие клавиш игрока
    if keys[pygame.K_w] and roket_y > 0:
        roket_y -= roket_speed

    # Снизу (y + высота < 400)
    if keys[pygame.K_s] and roket_y < 600 - roket_height:
        roket_y += roket_speed
    
    if ball_y > roket_ai_y:
        roket_ai_y += ai_roket_speed
    if ball_y < roket_ai_y:
        roket_ai_y -= ai_roket_speed
    
    my_roket = pygame.Rect(roket_x , roket_y , roket_width , roket_height)
    ai_roket = pygame.Rect(roket_ai_x , roket_ai_y , roket_ai_width , roket_ai_height)
    my_ball = pygame.Rect(ball_x , ball_y , ball_width , ball_height)
    
    pygame.draw.rect(screen , ("white") , my_roket)
    pygame.draw.rect(screen , ("white") , ai_roket)
    pygame.draw.rect(screen , ("white") , my_ball)
    
    my_text = font.render(f"Мой счет: {my_score}" , True , "white")
    ai_text = font.render(f"Счет бота: {ai_score}" , True , "white")
    
    screen.blit(my_text , (10 , 10))
    screen.blit(ai_text , (10 , 40))
    
    if ball_x <= 0:        # мяч улетел влево — очко ИИ
      ai_score += 1
      ball_x = 400
      ball_y = 300
      FPS = 60
      ai_roket_speed = 5
    if ball_x >= 800 - ball_width:  # мяч улетел вправо — очко игрока
      my_score += 1
      ball_x = 400
      ball_y = 300
      FPS = 60
      ai_roket_speed = 5
      
    
    
    
    if my_ball.colliderect(my_roket):
        ball_dx = -ball_dx
        FPS += 0.5
        roket_speed += 10
        ai_roket_speed += 1
        
    if my_ball.colliderect(ai_roket):
        ball_dx = -ball_dx
        FPS += 0.5
        roket_speed += 10
        ai_roket_speed += 1
        
    
    
    if roket_ai_y < 0:
      roket_ai_y = 0
    if roket_ai_y > 600 - roket_ai_height: 
      roket_ai_y = 600 - roket_ai_height
    

    
    
    
    
    
    clock.tick(FPS) 


    
    
    pygame.display.flip() #Обязательная штука чтобы была видна сама картинка игры а так просто нечего не будет видно
