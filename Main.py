import pygame 
import random
import math
import time

#initialisation of pygame
pygame.init()
AI_input = []

#Initialising Random variables
game_last_time = time.time()
Ai_last_time = time.time()
Movement_Of_Ai = ""

#create window
length_screen = 800
breadth_screen = 1000
screen = pygame.display.set_mode((breadth_screen,length_screen))

#Window personalisation 
pygame.display.set_caption("Snake EATS")
icon = pygame.image.load("Characters/Icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font(None, 20)

#region player
Player_Icon = pygame.image.load("Characters/Player Icon.png")
PlayerX = 500
PlayerY = 400
Player_rect = pygame.Rect(PlayerX,PlayerY,64,64)
Player_changeX = 0
Player_changeY = 0
Player_score = 0
score_text = font.render(f"Score: {Player_score}", True , (0,0,0))

def Player(x,y):
    screen.blit(Player_Icon,(x,y))
    Player_rect.x = x
    Player_rect.y = y

#endregion

#region Enemy
Enemy_Icon = pygame.image.load("Characters/rat.png")
EnemyX = random.randint(0,breadth_screen - 50)
EnemyY = random.randint(0,length_screen - 50)
Enemy_changeX = 0
Enemy_changeY = 0
Enemy_state = True
Enemy_count = 0

def Enemy_cood(Ex,Ey):
    Ex = random.randint(0,breadth_screen - 50)
    Ey = random.randint(0,length_screen - 50)
    return (Ex , Ey)

def Enemy(x,y):
    if Enemy_state:
        screen.blit(Enemy_Icon,(x,y))

#endregion

#region obstacle
Obstacle_icon = pygame.image.load("Characters/warning.png")
ObstacleX = []
ObstacleY = []
Obstacle_rect = []
obstacle_count = 1

for i in range(obstacle_count):
    ObstacleX.append(random.randint(0,breadth_screen - 50))
    ObstacleY.append(random.randint(0,length_screen - 50))
    Obstacle_rect.append(pygame.Rect(ObstacleX[i],ObstacleY[i],64,64))

def obstacle(x,y,i):
    screen.blit(Obstacle_icon , (x,y))
    Obstacle_rect[i].x = x
    Obstacle_rect[i].y = y

#endregion

#region Ai Inputs Variable
Player_X_Enemy = 0 # 1 is Right , 0 is Same , -1 is Left
Player_Y_Enemy = 0 # 1 is Up , 0 is Same , -1 is Down
Player_X_Obstacle = []
Player_Y_Obstacle = []
Player_Obstacle_distance = []

def score(x,y):
    screen.blit(score_text, (x,y))

#Game loop
Running = True
while Running:

    # Background
    screen.fill((255,255,255))

    #region Movements
    PlayerX += Player_changeX
    PlayerY += Player_changeY

    # Movements Restrictions
    if PlayerX >= breadth_screen - 50:
        PlayerX = breadth_screen - 50
    elif PlayerX <= 0:
            PlayerX = 0

    if PlayerY >= length_screen - 50:
       PlayerY = length_screen - 50
    elif PlayerY <= 0:
        PlayerY = 0
    
    Player_rect.x = PlayerX
    Player_rect.y = PlayerY
    for i in range(obstacle_count):
        if Player_rect.colliderect(Obstacle_rect[i]):
            PlayerX -= Player_changeX
            PlayerY -= Player_changeY
    #endregion

    #region collision detection for enemy
    collision_distance = math.hypot(PlayerX -EnemyX , PlayerY - EnemyY)
    if (collision_distance <= 48):
        Enemy_state = False
        Player_score += 10
        score_text = font.render(f"Score: {Player_score}", True , (0,0,0))
        print(Player_score)
    #endregion
    
    #region Screen
    Player(PlayerX ,PlayerY)
    Enemy(EnemyX , EnemyY)
    score(10,10)
    for i in range(obstacle_count):
        obstacle(ObstacleX[i],ObstacleY[i], i)
    pygame.display.update()

    if (Enemy_state == False):
        EnemyX, EnemyY =  Enemy_cood(EnemyX, EnemyY)
        Enemy_state = True

    #endregion

    #For Events in the game
    for Event in pygame.event.get():
        #region movements
        if Event.type == pygame.KEYDOWN:
            if Event.key == pygame.K_LEFT:
                Movement_Of_Ai = "Left"
                print("L")
            if Event.key == pygame.K_RIGHT:
                Movement_Of_Ai = "Right"
                print("R")
            if Event.key == pygame.K_UP:
                Movement_Of_Ai = "Up"
                print("U")
            if Event.key == pygame.K_DOWN:
                Movement_Of_Ai = "Down"
                print("D")
            if Event.key == pygame.K_SPACE:
                Movement_Of_Ai = ''
                print("N")
        #endregion

        #End condition
        if Event.type == pygame.QUIT:
            Running = False

    #region Movement 
    if (Movement_Of_Ai == "Left"):
        Player_changeX = -0.4
    elif(Movement_Of_Ai == "Right"):
        Player_changeX = 0.4
    else:
        Player_changeX = 0
    
    if(Movement_Of_Ai == "Up"):
        Player_changeY = -0.4
    elif(Movement_Of_Ai == "Down"):
        Player_changeY = 0.4
    else:
        Player_changeY = 0
    #endregion

    #time randomness
    if (time.time() - game_last_time) >= 10:
        Enemy_state = False
        for i in range(obstacle_count):
            while True:
                x = random.randint(0,950)
                y = random.randint(0,750)
                new_rect = pygame.Rect(x,y,64,64)

                if not Player_rect.colliderect(new_rect):
                    break

            ObstacleX[i] = x
            ObstacleY[i] = y
            Obstacle_rect[i] = new_rect

        game_last_time = time.time()


    #region Ai input
    if  (time.time() - Ai_last_time >= 1):
        #Player co-odinates
        print(f"Player Location: {PlayerX} , {PlayerY}")

        #region Enemy info
        if Enemy_state:
            print(f"Rat Location: {EnemyX},{EnemyY}")


            print("X-Direction of Rat")
            X_Difference = (EnemyX-PlayerX)/breadth_screen*100
            if (abs(X_Difference) > 5):
                if (X_Difference>0):
                    Player_X_Enemy = 1 #Right
                else:
                    Player_X_Enemy = -1 #Left
            else:
                Player_X_Enemy = 0 #same

            
            print("Y-Direction of Rat")
            Y_Difference = (EnemyY - PlayerY)/length_screen*100
            if (abs(Y_Difference) > 5):
                if (Y_Difference > 0):
                    Player_Y_Enemy = -1 #Down
                else:
                    Player_Y_Enemy = 1 #Up
            else:
                Player_Y_Enemy = 0 #Same
        else:
            Player_X_Enemy = 0
            Player_Y_Enemy = 0
        #endregion


        #region Obstacle info
        for i in range(obstacle_count):
            Distance = math.hypot(ObstacleX[i]-PlayerX, ObstacleY[i] - PlayerY)

            if (Distance<100):
                Player_Obstacle_distance.append([i,Distance])

                print("X-Direction of obstacle")
                X_Difference = (ObstacleX[i]-PlayerX)/breadth_screen*100
                if (abs(X_Difference) > 5):
                    if (X_Difference > 0):
                        Player_X_Obstacle.append([i,1]) #Right
                    else:
                        Player_X_Obstacle.append([i,-1]) #Left
                else:
                    Player_X_Obstacle.append([i,0]) #Same

                print("Y-Direction of obstacle")
                Y_Difference = (ObstacleY[i]-PlayerY)/length_screen*100
                if (abs(Y_Difference) > 5):
                    if (Y_Difference>0):
                        Player_Y_Obstacle.append([i,-1]) #Down
                    else:
                        Player_Y_Obstacle.append([i,1]) #Up
                else:
                    Player_Y_Obstacle.append([i,0]) #same
        #endregion

        AI_input = ( PlayerX, PlayerY , EnemyX, EnemyY , Player_X_Enemy , Player_Y_Enemy , Player_X_Obstacle , Player_Y_Obstacle , Player_Obstacle_distance )
        Player_X_Obstacle = []
        Player_Y_Obstacle = []
        Player_Obstacle_distance = []
        
        Ai_last_time = time.time()

    #endregion


