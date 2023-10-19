import pygame
import sys
from pygame.locals import *
from Character import *

# Инициализация Pygame
pygame.init()

# Установка окна игры
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')

# Загрузка изображения фона
background_img = pygame.image.load('background.jpg')

# Создание объекта игрока
player = Player()

# Создание списка врагов
enemies = []
for i in range(6):
    enemy = Enemy()
    enemies.append(enemy)

# Создание списка пуль
bullets = []

# Основной игровой цикл
while True:
    screen.blit(background_img, (0, 0))  # Отрисовка фона

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Обработка движений игрока
        if event.type == KEYDOWN:
            player.handle_movement(event)

            # Обработка стрельбы игрока
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.x, player.y)
                bullets.append(bullet)

    # Границы движения игрока
    player.check_boundary()

    # Отрисовка игрока
    player.draw(screen)

    # Обновление позиции и отрисовка врагов
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    # Обновление позиции и отрисовка пуль
    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

        # Удаление пуль, которые вышли за пределы экрана
        if bullet.y < 0:
            bullets.remove(bullet)

    # Обновление экрана
    pygame.display.update()