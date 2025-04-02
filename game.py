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
        self.Score = 0
        self.paused = True
        self.pause_options = ["Resume", "Exit"]
        self.selected_index = 0
        self.showing_pause_menu = False

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

        # Boxes setup
        self.box_rows = 5
        self.box_cols = 8
        self.box_width = 50
        self.box_height = 20
        self.box_padding = 5
        self.boxes = [] 

        # 2D array of (rect, active)
        for row in range(self.box_rows):
            box_row = []
            for col in range(self.box_cols):
                x = col * (self.box_width + self.box_padding) + 40
                y = row * (self.box_height + self.box_padding) + 40
                rect = pygame.Rect(x, y, self.box_width, self.box_height)
                box_row.append([rect, True])
            self.boxes.append(box_row)

    def update(self):
        if self.paused:
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
        if self.ball_y <= 32:
            self.ball_dy *= -1

        # Collide with boxes
        ball_rect = pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size)
        for row in self.boxes:
            for box in row:
                rect, active = box
                if active and ball_rect.colliderect(rect):
                    box[1] = False
                    self.Score += 10
                    # Simple bounce logic: invert dy
                    if abs(self.ball_y + self.ball_size - rect.top) < 5 or abs(self.ball_y - rect.bottom) < 5:
                        self.ball_dy *= -1
                    else:
                        self.ball_dx *= -1
                    break

        # Collide with player 
        for i, rect in enumerate(self.blocks):
            ball_rect = pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size)
            if ball_rect.colliderect(rect):
                self.ball_dy *= -1
                if i == 0:
                    self.ball_dx = -4
                if i == 1:
                    self.ball_dx = random.choice([-3, -1])
                elif i == 2:
                    self.ball_dx = random.choice([-1, 1])
                elif i == 3:
                    self.ball_dx = random.choice([3, 1])
                elif i == 4:
                    self.ball_dx = 4
                break

    def render(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))

        # Draw top boundary and HUD
        pygame.draw.line(screen, WHITE, (0, 32), (480, 32), 2)
        title_surface = self.text_font.render("PYBREAKOUT", True, WHITE)
        screen.blit(title_surface, title_surface.get_rect(center=(240, 16)))
        score_surface = self.text_font.render(f"Score: {self.Score}", True, WHITE)
        screen.blit(score_surface, (360, 8))

        if self.showing_pause_menu:
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

        # Draw boxes
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        for row_index, row in enumerate(self.boxes):
            color = colors[min(row_index, len(colors)-1)]
            for rect, active in row:
                if active:
                    pygame.draw.rect(screen, color, rect)

        # Draw ball
        pygame.draw.rect(screen, self.ball_color, pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.showing_pause_menu:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.pause_options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.pause_options)
                    elif event.key == pygame.K_RETURN:
                        selected = self.pause_options[self.selected_index]
                        if selected == "Resume":
                            self.showing_pause_menu = False
                            self.paused = False
                        elif selected == "Exit":
                            return True
                else:
                    if event.key == pygame.K_RETURN:
                        self.paused = not self.paused
                    elif event.key == pygame.K_ESCAPE:
                        self.showing_pause_menu = True
                        self.paused = True
        return False
