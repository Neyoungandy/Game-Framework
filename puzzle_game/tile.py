# Tile class with movement and state
import pygame
from settings import *

class Tile:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.is_moving = False
        self.animation_speed = 10
        
    def draw(self, screen):
        # Draw tile background
        rect = pygame.Rect(
            self.x * TILE_SIZE + GRID_OFFSET_X,
            self.y * TILE_SIZE + GRID_OFFSET_Y,
            TILE_SIZE - TILE_PADDING,
            TILE_SIZE - TILE_PADDING
        )
        pygame.draw.rect(screen, TILE_COLOR, rect)
        pygame.draw.rect(screen, TILE_BORDER_COLOR, rect, 2)
        
        # Draw tile number
        if self.value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.value), True, TEXT_COLOR)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
    
    def move_to(self, new_x, new_y):
        self.target_x = new_x
        self.target_y = new_y
        self.is_moving = True
    
    def update(self):
        if self.is_moving:
            # Animate movement
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            
            if abs(dx) < 0.1 and abs(dy) < 0.1:
                self.x = self.target_x
                self.y = self.target_y
                self.is_moving = False
            else:
                self.x += dx * self.animation_speed * 0.01
                self.y += dy * self.animation_speed * 0.01
