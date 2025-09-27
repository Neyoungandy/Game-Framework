# Main game loop and window
import pygame
import sys
from settings import *
from grid import Grid
from tile import Tile

class PuzzleGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Puzzle Game")
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.running = True
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                # Handle tile movement
                self.grid.handle_keypress(event.key)
    
    def update(self):
        # Update game logic
        pass
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.grid.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PuzzleGame()
    game.run()
