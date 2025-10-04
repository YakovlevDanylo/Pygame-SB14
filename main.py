from pygame import *

init()

# Створення вікна
window_size = (1000, 800)
window = display.set_mode(window_size)
display.set_caption("Моя перша гра")

# Створення годинника для кадрів
clock = time.Clock()



# Ігровий цикл
while True:
    window.fill((0, 0, 0))
    # 1 - перевірка усіх подій
    for e in event.get():
        if e.type == QUIT:
            quit()

    # 2 - Малювання усіх об'єктів на екрані

    # 3 - Оновлення екрану
    display.update()
    clock.tick(60)
