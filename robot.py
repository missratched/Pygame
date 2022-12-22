import pygame
from pygame.sprite import Sprite
class Robot(Sprite):
    " " "A class to manage the Robot" " "

    def __init__(self, robot_game):
        " " "Initialize the robot and set it's starting position." " "
        super().__init__()
        self.screen = robot_game.screen
        self.screen_rect = robot_game.screen.get_rect()
        self.settings = robot_game.settings


        #Load the ship image and get it's rect.
        self.image = pygame.image.load('images/robot.bmp').convert()
        DEFAULT_IMAGE_SIZE = (70, 80)
        self.image_robot = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image_robot.get_rect()

        #Start each new robot at the chosen location on the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the robot's horizontal position.
        self.x = float(self.rect.x)

        #Store a decimal value for the robot's vertical position.
        self.y = float(self.rect.y)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def center_robot(self):
        " " "Center the robot on the screen." " "
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        " " "Update the robot's position based on the movement flag" " "
        #Update the robot's value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.robot_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.robot_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.robot_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.robot_speed

        #Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y



    def blitme(self):
         " " "Draw the robot at its current location." " "
         self.screen.blit(self.image_robot, self.rect)
