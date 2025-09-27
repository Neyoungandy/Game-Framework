# Helper functions (e.g., save/load game)
import json
import os
from settings import *

def save_game(grid_state, filename="savegame.json"):
    """Save the current game state to a JSON file"""
    try:
        game_data = {
            "grid": grid_state,
            "empty_x": grid_state["empty_x"],
            "empty_y": grid_state["empty_y"]
        }
        
        with open(filename, 'w') as f:
            json.dump(game_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False

def load_game(filename="savegame.json"):
    """Load game state from a JSON file"""
    try:
        if not os.path.exists(filename):
            return None
            
        with open(filename, 'r') as f:
            game_data = json.load(f)
        return game_data
    except Exception as e:
        print(f"Error loading game: {e}")
        return None

def get_grid_state(grid):
    """Convert grid object to serializable state"""
    state = {
        "tiles": [],
        "empty_x": grid.empty_x,
        "empty_y": grid.empty_y
    }
    
    for y in range(GRID_HEIGHT):
        row = []
        for x in range(GRID_WIDTH):
            row.append(grid.tiles[y][x].value)
        state["tiles"].append(row)
    
    return state

def restore_grid_state(grid, state):
    """Restore grid from saved state"""
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid.tiles[y][x].value = state["tiles"][y][x]
    
    grid.empty_x = state["empty_x"]
    grid.empty_y = state["empty_y"]

def calculate_moves_to_solve(grid):
    """Calculate minimum moves needed to solve the puzzle"""
    # This is a simplified version - a real implementation would use A* or similar
    moves = 0
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            expected_value = y * GRID_WIDTH + x + 1
            if expected_value == GRID_WIDTH * GRID_HEIGHT:
                expected_value = 0
            
            if grid.tiles[y][x].value != expected_value:
                moves += 1
    
    return moves
