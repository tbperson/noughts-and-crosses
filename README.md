# Tic-Tac-Toe Game using Pygame

This Python script implements a simple Tic-Tac-Toe game using the Pygame library. The game features a graphical user interface where players can click on buttons to make their moves.

## Requirements

- Python 3.x
- Pygame library

## How to Run

1. Install Pygame library if you haven't already:

    ```
    pip install pygame
    ```

2. Run the script:

    ```
    python tic_tac_toe.py
    ```

3. The game window will open, and you can start playing by clicking on the buttons to make your moves.

## Gameplay

- The game starts with player 1 (X) making the first move.
- Players take turns clicking on the buttons to place their respective marks (X or O) on the board.
- The game ends when one player successfully aligns three marks horizontally, vertically, or diagonally, or when all buttons are clicked and there's no winner (a draw).
- If a player wins, the game window displays a message indicating the winning player (P1 or P2).
- If the game ends in a draw, the game window displays a draw message.

## Additional Features

- The game window updates to show whose turn it is (P1 or P2).
- There's a cheat feature enabled by pressing the 'R' key, which instantly declares the current player as the winner (this is commented out in the python file and must be uncommented to work)

## Customization

- You can modify the `window_width`, `window_height`, and `button_size` constants to adjust the size of the game window and buttons according to your preference.

## Credits

This script is created by [Your Name].

