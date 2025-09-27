// Puzzle Game JavaScript Implementation
class PuzzleGame {
    constructor() {
        this.board = [];
        this.emptyRow = 3;
        this.emptyCol = 3;
        this.moves = 0;
        this.startTime = Date.now();
        this.timer = null;
        this.isGameWon = false;
        
        this.initializeGame();
        this.renderBoard();
        this.startTimer();
        this.setupEventListeners();
    }
    
    initializeGame() {
        // Create solved board
        this.board = [];
        for (let i = 0; i < 4; i++) {
            this.board[i] = [];
            for (let j = 0; j < 4; j++) {
                this.board[i][j] = i * 4 + j + 1;
            }
        }
        this.board[3][3] = 0; // Empty space
        this.emptyRow = 3;
        this.emptyCol = 3;
    }
    
    shuffleGame() {
        // Shuffle the board
        for (let i = 0; i < 1000; i++) {
            const moves = this.getPossibleMoves();
            if (moves.length > 0) {
                const randomMove = moves[Math.floor(Math.random() * moves.length)];
                this.moveTile(randomMove.row, randomMove.col);
            }
        }
        this.moves = 0;
        this.startTime = Date.now();
        this.isGameWon = false;
        this.renderBoard();
        this.updateStats();
    }
    
    getPossibleMoves() {
        const moves = [];
        const directions = [
            { row: -1, col: 0 }, // Up
            { row: 1, col: 0 },  // Down
            { row: 0, col: -1 }, // Left
            { row: 0, col: 1 }    // Right
        ];
        
        for (const dir of directions) {
            const newRow = this.emptyRow + dir.row;
            const newCol = this.emptyCol + dir.col;
            
            if (newRow >= 0 && newRow < 4 && newCol >= 0 && newCol < 4) {
                moves.push({ row: newRow, col: newCol });
            }
        }
        
        return moves;
    }
    
    moveTile(row, col) {
        // Check if the tile can move to empty space
        const possibleMoves = this.getPossibleMoves();
        const canMove = possibleMoves.some(move => move.row === row && move.col === col);
        
        if (canMove) {
            // Swap tile with empty space
            this.board[this.emptyRow][this.emptyCol] = this.board[row][col];
            this.board[row][col] = 0;
            
            // Update empty position
            this.emptyRow = row;
            this.emptyCol = col;
            
            this.moves++;
            this.renderBoard();
            this.updateStats();
            this.checkWin();
        }
    }
    
    checkWin() {
        let isWon = true;
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                const expectedValue = i * 4 + j + 1;
                if (expectedValue === 16) expectedValue = 0;
                
                if (this.board[i][j] !== expectedValue) {
                    isWon = false;
                    break;
                }
            }
            if (!isWon) break;
        }
        
        if (isWon && !this.isGameWon) {
            this.isGameWon = true;
            this.showWinMessage();
        }
    }
    
    showWinMessage() {
        const winMessage = document.getElementById('winMessage');
        winMessage.style.display = 'block';
        
        // Hide message after 3 seconds
        setTimeout(() => {
            winMessage.style.display = 'none';
        }, 3000);
    }
    
    renderBoard() {
        const gameBoard = document.getElementById('gameBoard');
        gameBoard.innerHTML = '';
        
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                const tile = document.createElement('div');
                tile.className = 'tile';
                
                if (this.board[i][j] === 0) {
                    tile.className += ' empty';
                    tile.textContent = '';
                } else {
                    tile.textContent = this.board[i][j];
                    tile.onclick = () => this.moveTile(i, j);
                }
                
                gameBoard.appendChild(tile);
            }
        }
    }
    
    updateStats() {
        document.getElementById('moves').textContent = this.moves;
        
        const elapsed = Math.floor((Date.now() - this.startTime) / 1000);
        const minutes = Math.floor(elapsed / 60);
        const seconds = elapsed % 60;
        document.getElementById('time').textContent = 
            `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    startTimer() {
        this.timer = setInterval(() => {
            if (!this.isGameWon) {
                this.updateStats();
            }
        }, 1000);
    }
    
    setupEventListeners() {
        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            if (this.isGameWon) return;
            
            const moves = this.getPossibleMoves();
            let targetRow = this.emptyRow;
            let targetCol = this.emptyCol;
            
            switch(e.key) {
                case 'ArrowUp':
                    targetRow = this.emptyRow + 1;
                    break;
                case 'ArrowDown':
                    targetRow = this.emptyRow - 1;
                    break;
                case 'ArrowLeft':
                    targetCol = this.emptyCol + 1;
                    break;
                case 'ArrowRight':
                    targetCol = this.emptyCol - 1;
                    break;
                default:
                    return;
            }
            
            if (targetRow >= 0 && targetRow < 4 && targetCol >= 0 && targetCol < 4) {
                this.moveTile(targetRow, targetCol);
            }
        });
    }
    
    saveGame() {
        const gameState = {
            board: this.board,
            emptyRow: this.emptyRow,
            emptyCol: this.emptyCol,
            moves: this.moves,
            startTime: this.startTime
        };
        
        localStorage.setItem('puzzleGameSave', JSON.stringify(gameState));
        alert('Game saved!');
    }
    
    loadGame() {
        const saved = localStorage.getItem('puzzleGameSave');
        if (saved) {
            const gameState = JSON.parse(saved);
            this.board = gameState.board;
            this.emptyRow = gameState.emptyRow;
            this.emptyCol = gameState.emptyCol;
            this.moves = gameState.moves;
            this.startTime = gameState.startTime;
            
            this.renderBoard();
            this.updateStats();
            alert('Game loaded!');
        } else {
            alert('No saved game found!');
        }
    }
    
    resetGame() {
        this.initializeGame();
        this.moves = 0;
        this.startTime = Date.now();
        this.isGameWon = false;
        this.renderBoard();
        this.updateStats();
    }
}

// Global functions for buttons
let game;

function shuffleGame() {
    game.shuffleGame();
}

function resetGame() {
    game.resetGame();
}

function saveGame() {
    game.saveGame();
}

function loadGame() {
    game.loadGame();
}

// Initialize game when page loads
document.addEventListener('DOMContentLoaded', () => {
    game = new PuzzleGame();
});
