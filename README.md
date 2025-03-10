# snake-game
A simple yet fun snake game created using Python's turtle graphics library. This game allows the player to control a snake, eat food, and avoid collisions with walls or the snake's own body. The game keeps track of the score, which increases each time the snake eats the food.

# Table of Contents
. Installation
. How to Play
. Game Features
. Code Explanation
. Installation
. Prerequisites
. License

To run the game, you need to have Python and the turtle module installed on your system. The turtle module is included by default in most Python installations, but if you're missing it, you can install Python from here.

# Steps to Run the Game
. Clone or download the repository.
. Navigate to the project directory in your terminal or command prompt.
. Make sure all required files are in the same folder.

# Run the game using Python:

bash
python snake_game.py
This will open the game window, and you can start playing.

# How to Play
Use the arrow keys to control the snake's movement:

. Up Arrow: Move the snake upwards
. Down Arrow: Move the snake downwards
. Left Arrow: Move the snake left
. Right Arrow: Move the snake right

Your goal is to eat the food that appears on the screen. Each time you eat the food, the snake grows longer, and your score increases.

Avoid running into the walls or the snake's own body. If the snake collides with either, the game will reset, and your score will return to zero.

The game runs continuously until you close the window or the snake collides with an obstacle.

# Game Features
. Snake Movement: The snake moves in 4 directions (up, down, left, right).
. Growing Snake: Each time the snake eats food, it grows in size.
. Score Tracking: The game keeps track of your score, which increases as you eat more food.

# Game Over Conditions:
. If the snake collides with the wall.
. If the snake collides with its own body.
. Reset Functionality: When the snake collides with an obstacle, the game resets the snake and the score.

# Code Explanation
The game is implemented using Python's turtle module. Here's a breakdown of the key components of the game:

. Snakes: Defines the snake, its movement, and its ability to grow when it eats food.
. Food: Represents the food that the snake eats, randomly appearing on the screen.
. ScoreCard: Keeps track of the score and displays it on the screen.
. Screen: Sets up the game window, including its dimensions, background color, and title.
. Core Components
. Movement: Arrow keys control the snake's movement.
. Collision Detection: Detects collisions with the food, walls, and the snake's own body.

# License
This project is open-source and available under the MIT License. Feel free to modify and improve it for your own purposes!
