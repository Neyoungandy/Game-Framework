# Grid manager for tile layout and logic
import pygame
import random
from settings import *
from tile import Tile

class Grid:
    def __init__(self):
        self.tiles = []
        self.empty_x = GRID_WIDTH - 1
        self.empty_y = GRID_HEIGHT - 1
        self.initialize_tiles()
        self.shuffle_tiles()
        
    def initialize_tiles(self):
        """Initialize the grid with tiles in order"""
        self.tiles = []
        for y in range(GRID_HEIGHT):
            row = []
            for x in range(GRID_WIDTH):
                value = y * GRID_WIDTH + x + 1
                if value == GRID_WIDTH * GRID_HEIGHT:
                    value = 0  # Empty tile
                tile = Tile(value, x, y)
                row.append(tile)
            self.tiles.append(row)
    
    def shuffle_tiles(self):
        """Shuffle the tiles to create a solvable puzzle"""
        # Simple shuffle - in a real game, you'd want to ensure solvability
        for _ in range(1000):
            moves = self.get_possible_moves()
            if moves:
                move = random.choice(moves)
                self.move_tile(move)
    
    def get_possible_moves(self):
        """Get list of possible moves for the empty space"""
        moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            new_x = self.empty_x + dx
            new_y = self.empty_y + dy
            
            if (0 <= new_x < GRID_WIDTH and 
                0 <= new_y < GRID_HEIGHT):
                moves.append((new_x, new_y))
        
        return moves
    
    def move_tile(self, target_pos):
        """Move a tile to the empty position"""
        target_x, target_y = target_pos
        
        # Swap tile with empty space
        self.tiles[self.empty_y][self.empty_x].value = self.tiles[target_y][target_x].value
        self.tiles[target_y][target_x].value = 0
        
        # Update empty position
        self.empty_x = target_x
        self.empty_y = target_y
    
    def handle_keypress(self, key):
        """Handle keyboard input for tile movement"""
        moves = self.get_possible_moves()
        
        if key == pygame.K_UP and (self.empty_x, self.empty_y + 1) in moves:
            self.move_tile((self.empty_x, self.empty_y + 1))
        elif key == pygame.K_DOWN and (self.empty_x, self.empty_y - 1) in moves:
            self.move_tile((self.empty_x, self.empty_y - 1))
        elif key == pygame.K_LEFT and (self.empty_x + 1, self.empty_y) in moves:
            self.move_tile((self.empty_x + 1, self.empty_y))
        elif key == pygame.K_RIGHT and (self.empty_x - 1, self.empty_y) in moves:
            self.move_tile((self.empty_x - 1, self.empty_y))
    
    def is_solved(self):
        """Check if the puzzle is solved"""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                expected_value = y * GRID_WIDTH + x + 1
                if expected_value == GRID_WIDTH * GRID_HEIGHT:
                    expected_value = 0
                if self.tiles[y][x].value != expected_value:
                    return False
        return True
    
    def draw(self, screen):
        """Draw the grid and all tiles"""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.tiles[y][x].value != 0:
                    self.tiles[y][x].draw(screen)
