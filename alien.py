import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    " " "A class to represent a single alien in the fleet." " "


    def __init__(self, robot_game):
        " " "Initialize the alien and set its starting position." " "
        super().__init__()
        self.screen = robot_game.screen
        self.settings = robot_game.settings


        #Load the alien image and set it's rect attribute.
        self.image = pygame.image.load('images/alien.bmp').convert()
        DEFAULT_IMAGE_SIZE = (100, 100)
        self.image_alien = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image_alien.get_rect()

        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        " " "Return True if alien is at either edge of screen" " "
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        " " "Move the alien right or left" " "
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x




