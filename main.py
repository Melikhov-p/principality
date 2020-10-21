import pygame
import os, pygame
from colors import *
from settings import *

#Классы
class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.rect = self.image.get_rect()
        self.rect.left = xpos
        self.rect.top = HEIGHT - HEIGHT / 3 - 12
        self.speedx = 0

# Формирование земли
ground = [Ground(0), Ground(620), Ground(1240)]
for i in range(3):
    all_sprites.add(ground[i])

# Цикл игры
running = True
while running:
    screen.fill(BLACK)
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    #События
    for event in pygame.event.get():
        # закрытие окна с игрой
        if event.type == pygame.QUIT:
            running = False


    #Клавиши
    if keys[pygame.K_ESCAPE]: # ESC - выход
        running = False

    # Обновление
    all_sprites.update()
    # Рисовка
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()