import pygame
from Settings import Settings as St
import Game_functions as Gf
from pygame.sprite import Group

pygame.init()

crosses_gr=Group()
zeros_gr=Group()

# Инстанцируем настройки
settings_obj=St()

# Инициализируем экран
screen=pygame.display.set_mode((settings_obj.screen_width, settings_obj.screen_height))
pygame.display.set_caption(settings_obj.screen_caption)
bg_color=settings_obj.screen_color
screen_rect=screen.get_rect()

# Шрифт текста
font_=pygame.font.Font(None, 80)

# Создаем группу клеток
cell_side=(screen_rect.w-settings_obj.line_width*(settings_obj.board_size-1))//settings_obj.board_size
cells_gr=[]
Gf.Do_cells_gr(screen, screen_rect, settings_obj, cells_gr, cell_side)

while True:
    Gf.Check_events(screen, screen_rect, settings_obj, cell_side, cells_gr, crosses_gr, zeros_gr)
    Gf.Screen_draw(screen, screen_rect, bg_color, settings_obj, cells_gr, crosses_gr, zeros_gr, font_)
