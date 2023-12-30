from pygame import display, init


class GameDisplay:
    init()

    def __init__(self, size=tuple(display.get_desktop_sizes()), caption='Gomoku'):
        self.size = size
        self.caption = caption

    def run(self):
        game_display = display.set_mode(self.size)
        display.set_caption(self.caption)

        return game_display
