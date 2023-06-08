import pyxel
import random

class Menu():
    def __init__(self):
        pyxel.init(128, 128, "Snake by NextTap", 60)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            Jeu()

    def draw(self):
        pyxel.cls(11)
        pyxel.text(128 // 2 - 40, 128 // 2 - 5, 'Press [SPACE] to play', 7)

class Jeu:
    def __init__(self):
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.score = 0
        self.game_over = False
        self.snake = [(3, 0), (2, 0), (1, 0), (0, 0)]
        self.direction = "RIGHT"
        self.apple = self.generate_apple()
        self.frame_count = 0
        self.snake_speed = 5

    def generate_apple(self):
        while True:
            apple = (random.randint(0, 7), random.randint(0, 7))
            if apple not in self.snake:
                return apple

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.reset()
            return

        self.frame_count += 1
        if self.frame_count % self.snake_speed == 0:
            if pyxel.btn(pyxel.KEY_UP) and self.direction != "DOWN":
                self.direction = "UP"
            elif pyxel.btn(pyxel.KEY_DOWN) and self.direction != "UP":
                self.direction = "DOWN"
            elif pyxel.btn(pyxel.KEY_LEFT) and self.direction != "RIGHT":
                self.direction = "LEFT"
            elif pyxel.btn(pyxel.KEY_RIGHT) and self.direction != "LEFT":
                self.direction = "RIGHT"

            head = self.snake[0]
            if self.direction == "UP":
                new_head = (head[0], head[1] - 1)
            elif self.direction == "DOWN":
                new_head = (head[0], head[1] + 1)
            elif self.direction == "LEFT":
                new_head = (head[0] - 1, head[1])
            elif self.direction == "RIGHT":
                new_head = (head[0] + 1, head[1])

            if (
                new_head[0] < 0
                or new_head[0] > 31
                or new_head[1] < 0
                or new_head[1] > 31
                or new_head in self.snake
            ):
                self.game_over = True
                return

            self.snake.insert(0, new_head)

            if new_head == self.apple:
                self.score += 1
                self.apple = self.generate_apple()
                self.snake.insert(0, new_head)
            else:
                self.snake.pop()

    def draw(self):
        pyxel.cls(11)

        for segment in self.snake:
            pyxel.rect(segment[0] * 4, segment[1] * 4, 4, 4, 3)

        pyxel.rect(self.apple[0] * 4, self.apple[1] * 4, 4, 4, 8)

        if self.game_over:
            pyxel.text(128 // 2 - 15, 128 // 2 - 10 , "GAME OVER", 7)
            pyxel.text(128 // 2 - 45, 128 // 2 , "Press [SPACE] to restart", 7)
        else:
            pyxel.text(10, 10, "Score: {}".format(self.score), 7)

Menu()
