import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
    " " "A class to manage bullets fired from the robot." " "


    def __init__(self, robot_game):
        " " "Create a flower object at the robot's current position" " "
        super().__init__()
        self.screen = robot_game.screen
        self.settings = robot_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0, 0) and then set correct position..
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,\
        self.settings.bullet_height)
        self.rect.midtop = robot_game.robot.rect.midtop
       

        #Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        " " "Move the bullet up the screen." " "
        #Update the decimal position of the flower.
        self.y -= self.settings.bullet_speed
        #Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        " " "Draw the flower to it's current position" " "
        pygame.draw.rect(self.screen, self.color, self.rect)

