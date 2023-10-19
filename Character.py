import pygame
import random

player_img = pygame.image.load('Hero.png')
enemy_img = pygame.image.load('Enemies.png')
bullet_img = pygame.image.load('bullet.jpg')

# Класс игрока
class Player:
    def __init__(self):
        self.image = player_img
        self.x = 370
        self.y = 480

    def handle_movement(self, event):
        if event.key == pygame.K_LEFT:
            self.x -= 5
        elif event.key == pygame.K_RIGHT:
            self.x += 5

    def check_boundary(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Класс врага
class Enemy:
    def __init__(self):
        self.image = enemy_img
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)

    def move(self):
        self.y += 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Класс пули
class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.x = x + 16
        self.y = y - 24

    def move(self):
        self.y -= 5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))