from random import randint

from pygame import *

init()

# Створення вікна
window_size = (1000, 800)
window = display.set_mode(window_size)
display.set_caption("Моя перша гра")

# Створення годинника для кадрів
clock = time.Clock()



class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.dx = speed
        self.dy = speed
        self.radius = radius
        self.color = color
        self.ball_rect = Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def reset(self):
        draw.circle(window, self.color, (self.x, self.y), self.radius)

    def collision(self, target):
        if self.ball_rect.colliderect(target):
            return True
        return False
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.ball_rect.x = self.x - self.radius
        self.ball_rect.y = self.y - self.radius

        if self.x > 1000 - self.radius or self.x <= 0 + self.radius:
            self.dx *= -1
        if self.y <= 0:
            self.dy *= -1
            self.dy += randint(1, 2)
        if self.y >= 800 - self.radius:
            self.dy *= -1


    def load_level(self, filename):
        blocks = []
        with open(filename) as map:
            lines = [line for line in map.readlines()]

        for row_index, line in enumerate(lines):
            for col_index, char in enumerate(line):
                if char == "1":
                    x = col_index * 50
                    y = row_index * 50
                    block = Rect(x, y, 45, 45)
                    blocks.append(block)
        return blocks


ball = Ball(100, 100, 10, (255, 0, 0), 5)

blocks = ball.load_level("level1.txt")
while True:
    window.fill((0, 0, 0))
    # 1 - перевірка усіх подій
    for e in event.get():
        if e.type == QUIT:
            quit()

    # 2 - Малювання усіх об'єктів на екрані

    for block in blocks:
        if ball.collision(block):
            blocks.remove(block)
        else:
            draw.rect(window, (145,152, 123), block)

    ball.update()
    ball.reset()

    # 3 - Оновлення екрану
    display.update()
    clock.tick(60)
