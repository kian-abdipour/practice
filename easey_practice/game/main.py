import pygame
from display import Display
from color import Color

game_display = Display.run()

progress = True
while progress:
    game_display.fill(Color.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            progress = False
    pygame.display.update()


pygame.quit()

