import pygame
import os
import random

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
        self.title_font = pygame.font.Font(FONT_PATH, 32)

        # game logic
        self.isPaused = True
        self.inPauseMenu = False
        self.pause_options = ["Resume", "Exit"]
        self.selected_index = 0

        # Player setup
        self.block_width = 20
        self.block_height = 10
        self.block_color = WHITE
        self.num_blocks = 5
        self.blocks = []
        self.center_x = 240
        self.y = 440

        # build player segments
        start_x = self.center_x - (self.num_blocks * self.block_width) // 2
        for i in range(self.num_blocks):
            rect = pygame.Rect(start_x + i * self.block_width, self.y, self.block_width, self.block_height)
            self.blocks.append(rect)

        # Ball setup
        self.ball_size = 10
        self.ball_x = 235
        self.ball_y = 300
        self.ball_color = WHITE
        self.ball_dx = 3
        self.ball_dy = 3

    def update(self):
        if self.isPaused or self.inPauseMenu:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for rect in self.blocks:
                rect.x -= 5
        if keys[pygame.K_RIGHT]:
            for rect in self.blocks:
                rect.x += 5

        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off window edges
        if self.ball_x <= 0 or self.ball_x + self.ball_size >= 480:
            self.ball_dx *= -1
        if self.ball_y <= 0:
            self.ball_dy *= -1

        # Collide with player 
        for i, rect in enumerate(self.blocks):
            ball_rect = pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size)
            if ball_rect.colliderect(rect):
                self.ball_dy *= -1
                if i in [0, 1]:
                    self.ball_dx = -4
                elif i == 2:
                    self.ball_dx = random.choice([-2, 2])
                elif i in [3, 4]:
                    self.ball_dx = 4
                break

    def render(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))

        if self.inPauseMenu:
            title_surface = self.title_font.render("Paused", True, WHITE)
            screen.blit(title_surface, title_surface.get_rect(center=(240, 150)))

            for i, option in enumerate(self.pause_options):
                color = WHITE if i == self.selected_index else (128, 128, 128)
                option_surface = self.text_font.render(option, True, color)
                screen.blit(option_surface, option_surface.get_rect(center=(240, 220 + i * 40)))
            return

        # Draw player blocks
        for rect in self.blocks:
            pygame.draw.rect(screen, self.block_color, rect)

        # Draw ball
        pygame.draw.rect(screen, self.ball_color, pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.inPauseMenu:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.pause_options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.pause_options)
                    elif event.key == pygame.K_RETURN:
                        selected_index = self.pause_options.index(self.pause_options[self.selected_index])
                        selected = self.pause_options[selected_index]
                        if selected == "Resume":
                            self.inPauseMenu = False
                            self.isPaused = False
                        elif selected == "Exit":
                            return True
                else:
                    if event.key == pygame.K_RETURN:
                        self.isPaused = not self.isPaused
                    elif event.key == pygame.K_ESCAPE:
                        self.inPauseMenu = True
                        self.isPaused = True
        return False