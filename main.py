import pygame
import os
from pygame.locals import *
from menu import MainMenu

# Initialize Pygame
def main():
    pygame.init()
    display = (480, 480)
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("PyBreakout")

    clock = pygame.time.Clock()
    running = True
    isGame = False

    menu = MainMenu()
    # game = Game()  # To be defined later

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                running = False

        if isGame:
            # game.handle_events(events)
            # game.update()
            # game.render()
            pass
        else:
            menu.handle_events(events)
            menu.update()
            menu.render()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()