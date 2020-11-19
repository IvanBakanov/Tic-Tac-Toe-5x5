class Settings():
    def __init__(self):
        # Настройки экрана игры
        self.screen_width=600
        self.screen_height=600
        self.screen_caption='Tic-Tac-Toe'
        self.screen_color=(250, 250, 250)

        # Настройки поля
        self.board_size=20
        self.line_color=(50, 50, 50)
        self.line_width=2

        # Настройки спрайтов
        self.cross_color=(178, 34, 34)
        self.zero_color=(72, 61, 139)
