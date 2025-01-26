from 方法 import *
import pygame
import time

oldy = 311
pygame.init()
pygame.key.stop_text_input()
pygame.key.set_repeat(10, 15)
screen = pygame.display.set_mode([800, 600])
run = True
tupian = pygame.image.load("曼.png").convert_alpha()
bgimage = pygame.image.load('背景.png').convert_alpha()
lb = pygame.image.load("火球.png").convert_alpha()
rb = pygame.transform.flip(lb, True, False)
hhh = man(tupian, 8, 1)
bg = kun(bgimage, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
fps = 16                 #帧率===================================
x = 400
y = 300
nx = x - hhh.rect.width / 2
ny = y - hhh.rect.height / 2
you = True
img = hhh.image
img2 = pygame.transform.flip(img, True, False)
diff = 30
jump = False
x = 400
y = 311
fonts = pygame.font.Font(None, 30)
zuobian = False
right = True
fashe = False
group = pygame.sprite.Group()
last_fire_time = 0  # 上次发射火球的时间
fire_cooldown = 150  # 发射火球的冷却时间（毫秒）

while run:
    current_time = pygame.time.get_ticks()  # 获取当前时间
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hhh.bian()
                img = hhh.image
                nx += 3
                right = True
            if event.key == pygame.K_a:
                hhh.bian()
                img = img2
                nx += -3
                right = False
            if event.key == pygame.K_w:
                jump = True
            if event.key == pygame.K_SPACE:
                if current_time - last_fire_time > fire_cooldown:
                    fashe = True
                    last_fire_time = current_time  # 更新上次发射火球的时间

    left_ball = huoqiu(lb, -7, screen, nx-20, y+50.5-15)
    right_ball = huoqiu(rb, 7, screen, nx+20 , y+50.5-15)
    if nx <= 0:
        nx = 1
    if nx + hhh.rect.width >= 800:
        nx = 799 - hhh.rect.width

    if jump:
        y -= diff
        diff -= 5
        if y == oldy:
            jump = False
            diff = 30


    screen.fill((0, 0, 0))
    bg.update()
    screen.blit(bg.image, bg.rect)
    if fashe and right:
        group.add(right_ball)
        hhh.bian()
        group.draw(screen)
        fashe = False  # 发射后立即设置fashe为False
    elif fashe and not right:
        group.add(left_ball)
        hhh.bian()
        group.draw(screen)
        fashe = False  # 发射后立即设置fashe为False
    group.update()

    screen.blit(img, (nx, y), hhh.rect)
    print_text(fonts, 0, 0, f"X:{nx}  Y:{y}")
    clock.tick(fps)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
