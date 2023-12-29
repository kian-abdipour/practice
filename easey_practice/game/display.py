from pygame import display, init


class Display:
    init()
    size = tuple(display.get_desktop_sizes())
    caption = 'kian'

    @classmethod
    def run(cls):
        game_display = display.set_mode(cls.size)
        display.set_caption(cls.caption)

        return game_display

