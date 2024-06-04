import pygame
import random
import os
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3
image_index = 0

IMAGE_PATH = "goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player_size = (12, 12)
player = pygame.image.load('player.png')
player_rect = player.get_rect(center=(WIDTH // 2, HEIGHT // 2)) 
player_speed = 5

def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.image.load('enemy.png')
    enemy_rect = pygame.Rect(WIDTH, random.randint(HEIGHT // 4, 3 * HEIGHT // 4 - enemy_size[1]), *enemy_size)
    enemy_speed = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_speed]

def create_bonus():
    bonus_size = (20, 20)
    bonus = pygame.image.load('bonus.png')
    bonus_rect = pygame.Rect(random.randint(WIDTH // 4, 3 * WIDTH // 4 - bonus_size[0]), 0, *bonus_size)
    bonus_speed = [0, random.randint(1, 6)]
    return [bonus, bonus_rect, bonus_speed]

pygame.time.set_timer(pygame.USEREVENT + 1, 1500)
pygame.time.set_timer(pygame.USEREVENT + 2, 2000)  
CHANGE_IMAGE = pygame.USEREVENT + 5
pygame.time.set_timer(CHANGE_IMAGE, 120)

enemies = []
bonuses = []

score = 0
lives = 3  # Додаємо змінну для відстеження кількості життів гравця
playing = True

while playing:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        elif event.type == pygame.USEREVENT + 1:
            enemies.append(create_enemy())
        elif event.type == pygame.USEREVENT + 2:
            bonuses.append(create_bonus())
        elif event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    bg_X1 -= bg_move
    bg_X2 -= bg_move

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    if bg_X1 < -bg.get_width():
        bg_X1 = bg_X2 + bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg_X1 + bg.get_width()

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(0, player_speed)
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_speed, 0)
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(0, -player_speed)
    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(-player_speed, 0)

    main_display.blit(player, player_rect)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            lives -= 1  # Зменшуємо кількість життів при зіткненні
            enemies.remove(enemy)  # Видаляємо ворога після зіткнення
            if lives == 0:
                playing = False  # Зупиняємо гру, якщо кількість життів дорівнює нулю
            break

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            bonuses.remove(bonus) 
            score += 5

    main_display.blit(FONT.render(f"Score: {score}", True, COLOR_BLACK), (WIDTH - 150, 20))
    main_display.blit(FONT.render(f"Lives: {lives}", True, COLOR_BLACK), (WIDTH - 150, 50))

    enemies = [enemy_data for enemy_data in enemies if enemy_data[1].right > 0]
    bonuses = [bonus_data for bonus_data in bonuses if bonus_data[1].bottom < HEIGHT]

    pygame.display.flip()
    
    pygame.time.delay(10)
