import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Pygame project')

walkRight = [pygame.image.load('data/pygame_right_1.png'),
pygame.image.load('data/pygame_right_2.png'), pygame.image.load('data/pygame_right_3.png'),
pygame.image.load('data/pygame_right_4.png'), pygame.image.load('data/pygame_right_5.png'),
pygame.image.load('data/pygame_right_6.png')]

walkLeft = [pygame.image.load('data/pygame_left_1.png'),
pygame.image.load('data/pygame_left_2.png'), pygame.image.load('data/pygame_left_3.png'),
pygame.image.load('data/pygame_left_4.png'), pygame.image.load('data/pygame_left_5.png'),
pygame.image.load('data/pygame_left_6.png')]

playerStand = pygame.image.load('data/pygame_idle.png')
bg = pygame.image.load('data/pygame_bg.jpg')

clock = pygame.time.Clock()

x = 0
y = 500 - 71 - 5
width = 60
height = 71
speed = 5
running = True
jump = False
jumpcount = 5
f = 0
left = False
right = False
animcount = 0


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def drawwin():
    global animcount
    win.blit(bg, (0, 0))
    if animcount + 1 >= 30:
        animcount = 0
    if left:
        win.blit(walkLeft[animcount // 5], (x, y))
        animcount += 1
    elif right:
        win.blit(walkRight[animcount // 5], (x, y))
        animcount += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()


while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < (500 - width - 5):
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animcount = 0
    if not(jump):
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpcount >= -5:
            if jumpcount < 0:
                y += (jumpcount ** 2) / 2
            else:
                y -= (jumpcount ** 2) / 2
            jumpcount -= 0.5
        else:
            jump = False
            jumpcount = 5

    drawwin()


pygame.quit()