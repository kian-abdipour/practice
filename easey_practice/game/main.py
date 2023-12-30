from pygame import event, QUIT, display, quit, draw
from game_display import GameDisplay
from color import Color

initialize_display = GameDisplay()
game_display = initialize_display.run()


progress = True
while progress:
    game_display.fill(Color.gray)
    draw.rect(game_display, Color.white, (1250, 470, 20, 20))
    for game_event in event.get():
        if game_event.type == QUIT:
            progress = False

    display.update()


quit()

