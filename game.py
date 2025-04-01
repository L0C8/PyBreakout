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
        # self.text = "[Paused]"
    
        # game logic
        self.isPaused = True

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
        if self.isPaused:
            return

        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Bounce off window edges
        if self.ball_x <= 0 or self.ball_x + self.ball_size >= 480:
            self.ball_dx *= -1
        if self.ball_y <= 0:
            self.ball_dy *= -1

        # Bounce off player
        for rect in self.blocks:
            if pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size).colliderect(rect):
                self.ball_dy *= -1
                break

    def render(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))

        # Draw return text
        text_surface = self.text_font.render(self.text, True, WHITE)
        screen.blit(text_surface, text_surface.get_rect(center=(240, 240)))

        # Draw player blocks
        for rect in self.blocks:
            pygame.draw.rect(screen, self.block_color, rect)

        # Draw ball
        pygame.draw.rect(screen, self.ball_color, pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.isPaused = not self.isPaused
                elif event.key == pygame.K_LEFT:
                    for rect in self.blocks:
                        rect.x -= 10
                elif event.key == pygame.K_RIGHT:
                    for rect in self.blocks:
                        rect.x += 10
                elif event.key == pygame.K_ESCAPE:
                    return True 
        return False
