# Puzzle Game

A sliding puzzle game built with Python and Pygame.

## Description

This is a classic sliding puzzle game where you need to arrange numbered tiles in order by sliding them into the empty space. The goal is to arrange the tiles from 1 to 15 in numerical order.

## Features

- Classic 4x4 sliding puzzle gameplay
- Smooth tile animations
- Save and load game functionality
- Keyboard controls (arrow keys)
- Clean, modern interface

## Installation

1. Make sure you have Python 3.6+ installed
2. Install required dependencies:
   ```bash
   pip install pygame
   ```

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Use arrow keys to move tiles:
   - ↑ Move tile up into empty space
   - ↓ Move tile down into empty space
   - ← Move tile left into empty space
   - → Move tile right into empty space

3. Press ESC to quit the game

## Game Controls

- **Arrow Keys**: Move tiles
- **ESC**: Quit game

## File Structure

- `main.py` - Main game loop and window
- `tile.py` - Tile class with movement and state
- `grid.py` - Grid manager for tile layout and logic
- `settings.py` - Game constants (screen size, tile size, etc.)
- `utils.py` - Helper functions (e.g., save/load game)
- `assets/` - Game assets (images and sounds)
- `savegame.json` - Optional file for saving game state

## Requirements

- Python 3.6+
- Pygame 2.0+

## License

This project is open source and available under the MIT License.
