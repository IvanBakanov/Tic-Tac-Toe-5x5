import pygame
from pygame.sprite import Sprite

class Cross(Sprite):
    def __init__(self, side, center_pos):
        super().__init__()
        self.image=pygame.image.load('Images/Cross.png')
        self.image=pygame.transform.scale(self.image, (side, side))
        self.rect=self.image.get_rect()
        self.rect.center=center_pos

    def draw(self):
        self.screen.blit(self.image, self.rect)
