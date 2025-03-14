import pygame
import sys
import math
from random import randint

FPS = 60
WIDTH = 800
HEIGHT = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class background:
    left_side = pygame.Surface((WIDTH / 2, HEIGHT))
    right_side = pygame.Surface((WIDTH / 2, HEIGHT))
    @staticmethod
    def draw():
        background.left_side.fill((0,0,0))
        background.right_side.fill((255,255,255))
        screen.blit(background.left_side, (0,0))
        screen.blit(background.right_side, (WIDTH / 2, 0))

class platforms():
    leftCords = [50, HEIGHT/2]
    rightCords = [760, HEIGHT/2]
    speed = 10
    width = 20
    height = 100
    leftRect = pygame.Rect(leftCords[0],leftCords[1],width,height)
    rightRect = pygame.Rect(rightCords[0],rightCords[1],width,height)

    @staticmethod
    def draw():
        pygame.draw.rect(screen, (255,255,255), platforms.leftRect)
        pygame.draw.rect(screen, (0,0,0), platforms.rightRect)

    @staticmethod
    def update():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not platforms.leftRect.y == 0:
            platforms.leftRect.y = platforms.leftRect.y - platforms.speed
        if keys[pygame.K_s] and not platforms.leftRect.y == HEIGHT - platforms.height:
            platforms.leftRect.y = platforms.leftRect.y + platforms.speed
        if keys[pygame.K_UP] and not platforms.rightRect.y == 0:
            platforms.rightRect.y = platforms.rightRect.y - platforms.speed
        if keys[pygame.K_DOWN] and not platforms.rightRect.y == HEIGHT - platforms.height:
            platforms.rightRect.y = platforms.rightRect.y + platforms.speed

class ball:
    surf = pygame.Surface((20,20), pygame.SRCALPHA)
    alpha = 60
    velocity = 5
    surf.fill((0,0,0,0))
    X = WIDTH / 2
    Y = HEIGHT / 2
    cooldown = 0
    @staticmethod
    def process():
        if ball.cooldown != 0:
            ball.cooldown -= 1
        if ball.Y <= 0 or ball.Y >= HEIGHT:
            ball.alpha = -1*ball.alpha
        rect = ball.surf.get_rect(topleft=(ball.X, ball.Y))
        if not ball.cooldown:
            if rect.colliderect(platforms.rightRect):
                ball.alpha = randint(120,240)
            if rect.colliderect(platforms.leftRect):
                ball.alpha = randint(-60,60)
        ball.X += math.cos(math.pi*ball.alpha/180*-1)*ball.velocity
        ball.Y += math.sin(math.pi*ball.alpha/180*-1)*ball.velocity
        screen.blit(ball.surf, (ball.X, ball.Y))
        pygame.draw.ellipse(ball.surf, (100,100,100), ball.surf.get_rect())

while True:
    background.draw()
    platforms.update()
    platforms.draw()
    ball.process()
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)