import pygame
from Class_cell import Cell
from Class_cross import Cross
from Class_zero import Zero

move=True
win=1
text=''
text_color=0
flag_win=False

def Win(who, settings_obj):
    global text
    global text_color
    if who=='cross':
        text_color=settings_obj.cross_color
    else:
        text_color=settings_obj.zero_color
    text=f'"{who}" win!'

def Aux_func(figure, cells_gr, settings_obj, numX, numY, mtblX, mtblY):
    global win
    global flag_win
    for i in range(4):
        try:
            if cells_gr[numX+i*mtblX][numY+i*mtblY]==figure:
                win+=1
            else:
                win=1
                break
        except:
            win=1
            break
                    
    if win==5:
        Win(figure, settings_obj)
        flag_win=True
    else:
        win=1
        
def Analysis(settings_obj, cells_gr):
    global win
    global flag_win
    win=1
    figure=''
    for x in range(settings_obj.board_size):
        if flag_win:
            break
        for y in range(settings_obj.board_size):
            if flag_win:
                break
            if cells_gr[x][y]=='cross':
                figure='cross'
            if cells_gr[x][y]=='zero':
                figure='zero'
            if len(figure)>=4:
                # ----- right dgnl -----
                Aux_func(figure, cells_gr, settings_obj, x-1, y-1, -1, -1)
                # ----- left dgnl -----
                Aux_func(figure, cells_gr, settings_obj, x+1, y-1, 1, -1)
                # ----- horizontal -----
                Aux_func(figure, cells_gr, settings_obj, x, y-1, 0, -1)
                # ----- vertical -----
                Aux_func(figure, cells_gr, settings_obj, x+1, y, 1, 0)
                
def Do_cells_gr(screen, screen_rect, settings_obj, cells_gr, cell_side):
    for x in range(settings_obj.board_size):
        cells_gr.append([])
        for y in range(settings_obj.board_size):
            cells_gr[x].append(Cell(screen, screen_rect, settings_obj, cell_side, x, y))
    
def Check_events(screen, screen_rect, settings_obj, cell_side, cells_gr, crosses_gr, zeros_gr):
    global coord
    global move
    global flag_win
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not flag_win:
            if event.button==1:
                x=int(pygame.mouse.get_pos()[0]//(cell_side+settings_obj.line_width))
                y=int(pygame.mouse.get_pos()[1]//(cell_side+settings_obj.line_width))
                cell=cells_gr[x][y]
                if cell!='cross' and cell!='zero':
                    if move:
                        crosses_gr.add(Cross(cell_side, cell.rect.center))
                        cells_gr[x][y]='cross'
                        move=False
                    else:
                        zeros_gr.add(Zero(cell_side, cell.rect.center))
                        cells_gr[x][y]='zero'
                        move=True
                    Analysis(settings_obj, cells_gr)
        if event.type==pygame.KEYDOWN and flag_win:
            if event.key==pygame.K_SPACE:
                cells_gr.clear()
                Do_cells_gr(screen, screen_rect, settings_obj, cells_gr, cell_side)
                crosses_gr.empty()
                zeros_gr.empty()
                move=True
                flag_win=False
                                
def Screen_draw(screen, scr_r, bg_color, settings_obj, cells_gr, crosses_gr, zeros_gr, font_):
    screen.fill(bg_color)
    # Рисуем сетку
    for i in range(settings_obj.board_size-1):
        pygame.draw.line(screen, settings_obj.line_color, (scr_r.w//settings_obj.board_size*(i+1), 0), (scr_r.w//settings_obj.board_size*(i+1), scr_r.h), settings_obj.line_width)
    for i in range(settings_obj.board_size-1):
        pygame.draw.line(screen, settings_obj.line_color, (0, scr_r.h//settings_obj.board_size*(i+1)), (scr_r.w, scr_r.h//settings_obj.board_size*(i+1)), settings_obj.line_width)    
    crosses_gr.draw(screen)
    zeros_gr.draw(screen)
    # Рисуем текст
    if flag_win:
        result_text=font_.render(text, True, text_color, settings_obj.screen_color)
        screen.blit(result_text, (scr_r.centerx-result_text.get_rect().w//2, scr_r.centery-result_text.get_rect().h//2))
    pygame.display.flip()
