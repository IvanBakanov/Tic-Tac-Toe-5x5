import pygame

class Cell():
    def __init__(self, screen, scr_r, settings_obj, side, posX, posY):
        self.screen=screen
        self.settings_obj=settings_obj
        self.position=f'({posX+1}, {posY+1})'
        self.rect=pygame.Rect(0, 0, side, side)
        self.rect.x, self.rect.y=scr_r.w//settings_obj.board_size*posX+settings_obj.line_width, scr_r.h//settings_obj.board_size*posY+settings_obj.line_width
