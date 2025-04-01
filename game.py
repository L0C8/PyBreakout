import pygame
import os

FONT_PATH = os.path.join("assets", "ndsbios.ttf")

# Color definitions
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

class Game:
    def __init__(self):
        self.text_font = pygame.font.Font(FONT_PATH, 24)
        self.text = "[return]"

        # Player setup
        self.block_width = 15
        self.block_height = 10
        self.block_color = WHITE
        self.num_blocks = 5
        self.blocks = []
        self.center_x = 240
        self.y = 440

        # sub-blocks for the Player
        start_x = self.center_x - (self.num_blocks * self.block_width) // 2
        for i in range(self.num_blocks):
            rect = pygame.Rect(start_x + i * self.block_width, self.y, self.block_width, self.block_height)
            self.blocks.append(rect)

    def update(self):
        pass

    def render(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))

        # Draw player 
        for rect in self.blocks:
            pygame.draw.rect(screen, self.block_color, rect)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                return True 
        return False
