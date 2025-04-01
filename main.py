import pygame
import os
from pygame.locals import *
from menu import MainMenu
from game import Game

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
    game = None

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                running = False

        if isGame:
            if game.handle_events(events):
                isGame = False
                menu = MainMenu()
            game.update()
            game.render()
        else:
            result = menu.handle_events(events)
            if result == "Start Game":
                isGame = True
                game = Game()
            elif result == "Exit":
                running = False
            menu.update()
            menu.render()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()