#Game Title: Runner Game
####Video Demo: https://www.youtube.com/watch?v=3XkZzGRrOuE
####Description:
Runner Game is a 2D endless runner where the player avoids obstacles that spawn at increasing speeds. The game ends upon collision with an obstacle.

How to Play:

Controls:
Left Arrow: Move left
Right Arrow: Move right
Goal: Avoid obstacles, increase your score, and reach higher levels.
Features:

Increasing Difficulty: Levels advance every 15 points, increasing obstacle speed and spawn rate.
Game Reset: Press SPACE to restart after a game over.
Files Included:

game.py: Main game logic.
test_game.py: Test file for core functions using pytest.
Functions:

main(): Starts the game loop.
move_player(keys): Handles player movement.
spawn_obstacle(): Randomly generates obstacles.
update_score(): Increases score and adjusts level/difficulty.
check_collision(): Detects collisions between player and obstacles.
test_game.py
Use pytest to run automated tests for main functions:

test_move_player(): Verifies player movement boundaries.
test_update_score(): Checks score increment and level adjustment.
test_check_collision(): Confirms collision detection logic.

My intention with this project was to create a game that captures the charm and nostalgia of the classic games many of us remember so fondly. Those games, despite often having simple graphics and straightforward gameplay mechanics, had a unique ability to engage players for hours on end. With only basic controls and easy-to-understand objectives, they didn’t need complex systems or dazzling graphics to captivate players—something about their simplicity made them endlessly enjoyable. Friends and family would gather around, taking turns, challenging each other, and always trying to beat one another’s high scores. Often, it wasn’t just about winning; it was about that excitement of trying “one more time” to set a new record or make it a little further than the last attempt.

In crafting this game, I wanted to recreate that same feeling of friendly competition and pure enjoyment. I aimed to design it so that anyone could pick it up and start playing without needing to read a long set of instructions or master a complicated control scheme. My hope is that it will spark that familiar urge to keep playing and improving, especially for those who love simple yet challenging games that you can’t easily put down.

I sincerely hope that my game brings you that joy and nostalgia and that you find it entertaining enough to play again and again. This project is the result of my efforts to build something memorable, and I hope it’s as enjoyable to play as it was for me to create. I would be thrilled if it’s enough to evoke even a fraction of the timeless fun that inspired me, and I look forward to seeing if others can appreciate the experience I aimed to capture.
