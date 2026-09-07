import pygame 
import random
import math
import time
from Player import player
from Ai_agent import Ai_agent

#Correct the observation parameters
def correct_obs(li: list)-> tuple:
    li[0] = int(li[0]/50)
    li[3] = int(li[3]/20)
    li[4] = int(li[4]/20)
    li[5] = int(li[5]/20)
    li[6] = int(li[6]/20) 

    return tuple(li)

#initialisation of pygame
pygame.init()
AI_input = []

#Initialising Random variables
game_last_time = time.time()
Ai_last_time = time.time()


#create window
length_screen = 800
breadth_screen = 1000
screen = pygame.display.set_mode((breadth_screen,length_screen))

#Window personalisation 
pygame.display.set_caption("Snake EATS")
icon = pygame.image.load("Sprites/Icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font(None, 20)

#region player

Player_Icon ="Sprites/Player Icon.png"
Player1 = player(Player_Icon , 500 , 400)
Player_score = 0
score_text = font.render(f"Score: {Player_score}", True , (0,0,0))
Agent = Ai_agent(0.9,0.0001 , 0.1 , 0.9 , 0.9)

#endregion

#region Enemy
Enemy_Icon = pygame.image.load("Sprites/rat.png")
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
Obstacle_icon = pygame.image.load("Sprites/warning.png")
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
obstacle_left_dist = []
obstacle_right_dist = []
obstacle_up_dist = []
obstacle_down_dist = []
Movement_Of_Ai = 0
Ai_reward = 0
Truncated = False
Episode_reward = 0
prev_AI_input = None
prev_action = None

def score(x,y):
    screen.blit(score_text, (x,y))

#Game loop
Running = True
while Running:

    # Background
    screen.fill((255,255,255))

    #region Movements
    Player1.x += Player1.change_x
    Player1.y += Player1.change_y

    # Movements Restrictions
    if Player1.x >= breadth_screen - 50:
        Player1.x = breadth_screen - 50
    elif Player1.x <= 0:
            Player1.x = 0

    if Player1.y >= length_screen - 50:
       Player1.y = length_screen - 50
    elif Player1.y <= 0:
        Player1.y = 0
    
    Player1.rect.x = Player1.x
    Player1.rect.y = Player1.y
    for i in range(obstacle_count):
        if Player1.rect.colliderect(Obstacle_rect[i]):
            Player1.x -= Player1.change_x
            Player1.y -= Player1.change_y
            Ai_reward -= 1
    #endregion

    #region collision detection for enemy
    collision_distance = math.hypot(Player1.x -EnemyX , Player1.y - EnemyY)
    if (collision_distance <= 48):
        Enemy_state = False
        Player_score += 10
        Ai_reward += 100
        score_text = font.render(f"Score: {Player_score}", True , (0,0,0))
        print(Player_score)
    #endregion
    
    #region Screen
    Player1.update(screen= screen)
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
                Movement_Of_Ai = 2 # Left
                print("L")
            if Event.key == pygame.K_RIGHT:
                Movement_Of_Ai = 3 # Right
                print("R")
            if Event.key == pygame.K_UP:
                Movement_Of_Ai = 1 # Up
                print("U")
            if Event.key == pygame.K_DOWN:
                Movement_Of_Ai = 4 # Down
                print("D")
            if Event.key == pygame.K_SPACE:
                Movement_Of_Ai = 0 # Stop
                print("N")
        #endregion

        #End condition
        if Event.type == pygame.QUIT:
            Running = False

    #region Movement 
    if (Movement_Of_Ai == 2):
        Player1.change_x = -0.4
    elif(Movement_Of_Ai == 3):
        Player1.change_x = 0.4
    else:
        Player1.change_x = 0
    
    if(Movement_Of_Ai == 1):
        Player1.change_y = -0.4
    elif(Movement_Of_Ai == 4):
        Player1.change_y = 0.4
    else:
        Player1.change_y = 0
    #endregion

    #time randomness
    if (time.time() - game_last_time) >= 10:
        Enemy_state = False

        Truncated = True
        Episode_reward = 0
        Ai_reward = 0

        for i in range(obstacle_count):
            while True:
                x = random.randint(0,950)
                y = random.randint(0,750)
                new_rect = pygame.Rect(x,y,64,64)

                if not Player1.rect.colliderect(new_rect):
                    break

            ObstacleX[i] = x
            ObstacleY[i] = y
            Obstacle_rect[i] = new_rect

        game_last_time = time.time()


    # Ai input
    if  (time.time() - Ai_last_time >= 0.1):
        #Player co-odinates
        # print(f"Player Location: {Player1.x} , {Player1.y}")

        #region Enemy info
        if Enemy_state:
            # print(f"Rat Location: {EnemyX},{EnemyY}")

            Player_Enemy_distance = math.hypot(Player1.x -EnemyX , Player1.y - EnemyY)
            # print(Player_Enemy_distance)

            # print("X-Direction of Rat")
            X_Difference = (EnemyX-Player1.x)/breadth_screen*100
            if (abs(X_Difference) > 5):
                if (X_Difference>0):
                    Player_X_Enemy = 1 #Right
                else:
                    Player_X_Enemy = -1 #Left
            else:
                Player_X_Enemy = 0 #same

            
            # print("Y-Direction of Rat")
            Y_Difference = (EnemyY - Player1.y)/length_screen*100
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
            x_distance = Player1.x-ObstacleX[i]
            y_distance = Player1.y-ObstacleY[i]
            Distance = math.hypot(x_distance, y_distance)

            if (Distance<200):

                if (x_distance>0):
                    obstacle_left_dist.append(x_distance)
                else:
                    obstacle_right_dist.append(abs(x_distance))

                if(y_distance>0):
                    obstacle_up_dist.append(y_distance)
                else:
                    obstacle_down_dist.append(abs(y_distance))
                    


        #endregion

        AI_input = correct_obs([ Player_Enemy_distance, Player_X_Enemy , Player_Y_Enemy , min(obstacle_left_dist , default= 200) , 
                    min(obstacle_up_dist , default= 200) , min(obstacle_right_dist , default= 200) , min(obstacle_down_dist , default= 200)])

        Movement_Of_Ai = Agent.get_action(AI_input)

        if prev_AI_input is not None:
            if (prev_AI_input[0] - AI_input[0]>0):
                                    Ai_reward += 5

            Truncated = Agent.Update(prev_action , Ai_reward , prev_AI_input , AI_input, Truncated)

        print(Truncated)

        Episode_reward += Ai_reward
        Ai_reward -= 1

        print(f"Ai Reward : {Ai_reward}")

        obstacle_up_dist , obstacle_right_dist , obstacle_left_dist , obstacle_down_dist = [] , [] , [] ,[]

        prev_AI_input = AI_input
        prev_action = Movement_Of_Ai

        Agent.decay_epsilon()
        
        Ai_last_time = time.time()
