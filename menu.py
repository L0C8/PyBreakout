import pygame
import os

FONT_PATH = os.path.join("assets", "ndsbios.ttf")
SEL = (255, 255, 255)   # selected 
USL = (148, 148, 148)   # unselected 

class MainMenu:
    def __init__(self):
        self.header_font = pygame.font.Font(FONT_PATH, 48)
        self.text_font = pygame.font.Font(FONT_PATH, 24)
        self.title = "PYBREAKOUT"
        self.options = ["Start Game", "Exit"]
        self.selected_index = 0
        self.option_rects = []
        self.calculate_rects()

    def calculate_rects(self):
        self.option_rects = []
        for i, option in enumerate(self.options):
            text_surface = self.text_font.render(option, True, SEL)
            rect = text_surface.get_rect(center=(240, 200 + i * 40))
            self.option_rects.append(rect)

    def update(self):
        pass

    def render(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))

        title_surface = self.header_font.render(self.title, True, SEL)
        screen.blit(title_surface, title_surface.get_rect(center=(240, 100)))

        for i, option in enumerate(self.options):
            if i == self.selected_index:
                color = SEL 
            else: 
                color = USL
            text_surface = self.text_font.render(option, True, color)
            screen.blit(text_surface, self.option_rects[i])

    def handle_events(self, events):
        for event in events:
            # set selected item
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                for i, rect in enumerate(self.option_rects):
                    if rect.collidepoint(mouse_pos):
                        self.selected_index = i
            # mouse clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, rect in enumerate(self.option_rects):
                    if rect.collidepoint(mouse_pos):
                        self.selected_index = i
                        return self.options[i]
            # keyboard controls 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.options[self.selected_index]
                elif event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
