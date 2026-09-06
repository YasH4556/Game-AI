
import pygame

class player():
    def __init__(self , icon:str , x: int , y :int ):
        self.icon = pygame.image.load(icon)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x , self.y , 64 , 64)
        self.change_x = 0
        self.change_y = 0


    def update(self , screen):
        screen.blit(self.icon , (self.x , self.y))
        self.rect.x = self.x
        self.rect.y = self.y
