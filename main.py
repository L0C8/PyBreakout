import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os

# Import local modules
from menu import MainMenu  # We'll define this in menu.py

# Import Assets
FONT_PATH = os.path.join("assets", "ndsbios.ttf")


# Initialize Pygame and OpenGL
def main():
    pygame.init()
    display = (480, 480)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    clock = pygame.time.Clock()
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
