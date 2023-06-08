# Snake Game

Snake Game is a classic arcade game implemented using the Pyxel library. Control a snake and try to eat as many apples as possible while avoiding collisions with the walls and your own tail. The game features a scoring system, game over screen, and the ability to restart the game.

## Controls

- Use the arrow keys (up, down, left, right) to control the snake's movement.
- Press the SPACE key to restart the game when in game over state.

## Gameplay

- The snake starts with a length of 4 segments and moves to the right.
- Control the snake's movement to navigate and eat the apples.
- Each time the snake eats an apple, its length increases and the player's score is incremented.
- The game ends if the snake collides with the walls or its own tail.
- The goal is to achieve the highest score possible.

## Customization

You can customize the game by modifying the source code:

- Adjust the game window size and title by changing the arguments in the `pyxel.init()` function call.
- Modify the game graphics and colors by editing the image and tilemap files provided.
- Change the snake speed and size by modifying the `self.snake_speed` and `pyxel.rect()` calls in the code.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This game was developed using the [Pyxel](https://github.com/kitao/pyxel) library.
