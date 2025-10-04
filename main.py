from pygame import *

init()

# Створення вікна
window_size = (1000, 800)
window = display.set_mode(window_size)
display.set_caption("Моя перша гра")

# Створення годинника для кадрів
clock = time.Clock()

class Block:
    def __init__(self, img_path, width, height):
        self.image = image.load(img_path)
        self.image = transform.scale(self.image, (width, height))
        self.height = height
        self.width = width
        # Створення хіт боксу
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        blocks.append(self)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

blocks = []
big_rock = Block("asset_level/big_rock.png", 150, 150)
medium_block = Block("asset_level/medium_rock.png", 150, 100)
for i in range(5):
    Block("asset_level/full_g_block.png", 200,60)
for i in range(5):
    Block("asset_level/full_h_block.png", 60,200)
for i in range(5):
    Block("asset_level/one_block.png", 60,60)
for i in range(5):
    Block("asset_level/little_bush.png", 60,60)
for i in range(5):
    Block("asset_level/little_leaf.png", 60,60)
for i in range(5):
    Block("asset_level/sprout_2.png", 60,60)
for i in range(5):
    Block("asset_level/big_stick.png", 150,250)


# Ігровий цикл
while True:
    window.fill((0, 0, 0))
    # 1 - перевірка усіх подій
    for e in event.get():
        if e.type == QUIT:
            quit()

    # 2 - Малювання усіх об'єктів на екрані
    for block in blocks:
        block.reset()

    # 3 - Оновлення екрану
    display.update()
    clock.tick(60)
