import pygame
import os

FONT_PATH = os.path.join("assets", "ndsbios.ttf")
SEL = (255, 255, 255)

class Game:
    def __init__(self):
        self.text_font = pygame.font.Font(FONT_PATH, 24)
        self.text = "[return]"

    def update(self):
        pass

    def render(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))
        text_surface = self.text_font.render(self.text, True, SEL)
        screen.blit(text_surface, text_surface.get_rect(center=(240, 240)))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                return True  # signal to return to main menu
        return False