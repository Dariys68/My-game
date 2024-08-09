# Simple Pygame Project

This is a simple game created using Pygame. The objective of the game is to control the player character, avoid enemies, and collect bonuses to score points. The game ends when the player loses all lives.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You also need to install the `pygame` library. You can install it via pip:

```bash
pip install pygame

How to Run
Clone this repository to your local machine:

bash

git clone https://github.com/yourusername/yourrepository.git
Navigate to the project directory:

bash

cd yourrepository
Run the game:

bash

python src/main.py

How to Play
Use the arrow keys to move the player character:
UP - Move up
DOWN - Move down
LEFT - Move left
RIGHT - Move right
Avoid the enemies and collect the bonuses.
The game ends when you lose all lives.
Your score is displayed at the top right of the screen.
Game Elements
Player: The character you control. Move it around the screen to avoid enemies and collect bonuses.
Enemies: Red objects that move towards the player from the right. Colliding with an enemy reduces the player's lives by one.
Bonuses: Green objects that fall from the top. Collecting a bonus increases your score by 5 points.
Code Overview
The main components of the game are:

Player Movement: The player can move in all directions using the arrow keys. The speed of the player is controlled by player_speed.
Enemies and Bonuses: These are generated at intervals and move across the screen. Enemies reduce the player's lives on collision, while bonuses increase the player's score.
Background: The background scrolls continuously to give the illusion of movement.