import pygame, os
# print('Выберите разрешение: 1 - 1440x900',
#       '2 - 1920x1080')
# resolution = input()
# if resolution == '1':
#     WIDTH = 1440
#     HEIGHT = 900
# else:
#     WIDTH = 1920
#     HEIGHT = 1080
WIDTH = 1440
HEIGHT = 900
FPS = 30

# Настройки
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Principality")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
DEBUG_MODE = False
font1 = pygame.font.Font(None, 36)
# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
# player_img = pygame.image.load(os.path.join(img_folder, 'BlackKnight.png'))
ground_img = pygame.image.load(os.path.join(img_folder, 'ground.png'))