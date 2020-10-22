import random
from colors import *
from settings import *


# Классы
class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.rect = self.image.get_rect()
        self.rect.left = xpos
        self.rect.top = HEIGHT - HEIGHT / 3 - 12

    def update(self, *args):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = 7
            if self.rect.left >= WIDTH:
                self.rect.right = 0
        if keys[pygame.K_RIGHT]:
            self.speedx = -7
            if self.rect.right <= 0:
                self.rect.left = WIDTH
        if keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT]:
            self.speedx = 12
        if keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]:
            self.speedx = -12
        self.rect.x += self.speedx

class Tree(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 300))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.top = HEIGHT / 3
        self.rect.x = xpos
        self.health = 100

    def get_damage(self, damage):
        self.health -= damage

    def die(self):
        self.rect.top = 0

    def respawn(self):
        self.rect.top = HEIGHT / 3
        self.health = 100

    def update(self, *args):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = 7
            if self.rect.left >= WIDTH:
                self.rect.right = 0
        if keys[pygame.K_RIGHT]:
            self.speedx = -7
            if self.rect.right <= 0:
                self.rect.left = WIDTH
        if self.health <= 0 and self.rect.x >= WIDTH or self.rect.right <= 0:
            self.respawn()
        self.rect.x += self.speedx

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH / 2
        self.rect.top = HEIGHT / 3 + 200
        self.health = 100
        self.stamina = 100
        self.damage = 15

    def get_damage(self, damage):
        self.health -= damage

    def die(self):
        you_died = font1.render('YOU DIED', 1, (RED))
        screen.blit(you_died, (WIDTH / 2 - 50, 200))

class Inventory():
    def __init__(self):
        self.tree = 0

    def draw_inventory(self):
        head = 'Inventory'
        draw_head = font1.render(head, 1, (WHITE))
        screen.blit(draw_head, (10, HEIGHT - 125))
        trees = 'Trees: ' + str(self.tree)
        draw_trees = font1.render(trees, 1, (WHITE))
        screen.blit(draw_trees,(10, HEIGHT - 100))

class Mob(pygame.sprite.Sprite):
    def __init__(self, mob_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.top = player.rect.top
        self.rect.left = 100
        self.rect.left = mob_pos
        self.rect.top = HEIGHT / 3 + 200
        self.health = 100
        self.damage = 5
        self.speed = 5

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = 6
        if keystate[pygame.K_RIGHT]:
            self.speedx = -6
        if keystate[pygame.K_LSHIFT] and keystate[pygame.K_LEFT]:
            self.speedx = 12
        if keystate[pygame.K_LSHIFT] and keystate[pygame.K_RIGHT]:
            self.speedx = -12
        self.rect.x += self.speedx

    def get_damage(self, damage):
        self.health -= damage

    def die(self):
        self.rect.top = 0

    def respawn(self, mob_pos_x):
        self.rect.top = HEIGHT / 3 + 200
        self.rect.left = mob_pos_x
        self.health = 100

#Деревья
trees = [Tree(0), Tree(440), Tree(880), Tree(1250)]
for i in range(4):
        all_sprites.add(trees[i])

# Добавляем игрока и его атрибуты(здоровье и т.п.)
player = Player()
inventory = Inventory()
all_sprites.add(player)

# Mobs
mob = Mob(100)
all_sprites.add(mob)

# Формирование земли
if WIDTH == 1440 and HEIGHT == 900:
    ground = [Ground(0), Ground(640), Ground(1280), Ground(1920)]
    for i in range(4):
        all_sprites.add(ground[i])

# Цикл игры
running = True
while running:
    screen.fill(BLACK)
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    screen.blit(bg, (0, 0))
    # События
    for event in pygame.event.get():
        # закрытие окна с игрой
        if event.type == pygame.QUIT:
            running = False

    if mob.rect.x <= -1000:  # Если моб уходит далеко за границы экрана перебрасываем его в другую сторону и ближе
        mob.respawn(1999)
    if mob.rect.x >= 2000:
        mob.respawn(-1000)

    # Клавиши
    if keys[pygame.K_ESCAPE]:  # ESC - выход
        running = False
    if keys[pygame.K_k]:
        player.die()

    # Удар/рубка дерева
    if not (isAttack):
        if keys[pygame.K_LCTRL]:
            isAttack = True
            if (mob.rect.x-player.rect.x) <= 100 and (mob.rect.x-player.rect.x) >= -100 and mob.rect.top != 0 and player.rect.y >= 500:
                mob.get_damage(player.damage)
                if mob.health <= 0:
                    mob.die()
        if keys[pygame.K_b]:
            isAttack = True
            for tree in trees:
                if (tree.rect.x - player.rect.x) <= 100 and (tree.rect.x-player.rect.x) >= -100:
                    tree.get_damage(player.damage*2)
                    if tree.health <= 0:
                        tree.die()
                        inventory.tree += random.randrange(5, 10, 1)
    else:
        if attackTimer >= 0:
            attackTimer -= 1
        else:
            isAttack = False
            attackTimer = 15

    # Прыжок
    if not (isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -11:
            if jumpCount < 0:
                player.rect.y += 9
            else:
                player.rect.y -= 9
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # Обновление
    all_sprites.update()
    # Рисовка
    all_sprites.draw(screen)
    inventory.draw_inventory()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()