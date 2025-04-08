import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

GREY = (125, 125, 125)
GREEN = (0, 163, 108)

cat_img = pygame.image.load("character.png")
cat_img = pygame.transform.smoothscale(cat_img, (50, 50))
cat = cat_img.get_rect()
cat.topleft = (100, 100)

background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (800, 600))

speed = 0
gravity = 0.5
jump_speed = -8

obstracle_timer = 0
obstracles = []
obstracles_width = 50
gap_height = 150
min_distance = 250
score = 0 
font = pygame.font.Font(None, 36)

while True:
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed
    speed += gravity
    cat.y += speed
    if cat.y > 500:
        cat.y = 550
        speed = 0
        pygame.quit()
    if cat.y < -70:
        cat.y = 550
        speed = 0 
        pygame.quit()
    obstracle_timer += 1
    if obstracle_timer > min_distance:
        top_obstracle_height = random.randint(100, 400)
        bottom_obstracle_height = screen.get_height() - top_obstracle_height - gap_height
        top_obstracle = pygame.Rect(800, 0, obstracles_width, top_obstracle_height)
        bottom_obstracle = pygame.Rect(800, screen.get_height() - bottom_obstracle_height, obstracles_width, bottom_obstracle_height)
        obstracles.append((top_obstracle, bottom_obstracle))
        obstracle_timer = 0

    for top_obstracle, bottom_obstracle in obstracles:
        top_obstracle.x -= 5
        bottom_obstracle.x -= 5
        if cat.colliderect(top_obstracle) or cat.colliderect(bottom_obstracle):
            print("Game Over!")
            print(f"Кількість очок: {score}")
            pygame.quit()
            exit()
        if top_obstracle.x < -obstracles_width:
            score += 1
            obstracles.remove((top_obstracle, bottom_obstracle))

    screen.blit(cat_img, cat.topleft)
    for top_obstracle, bottom_obstracle in obstracles:
        pygame.draw.rect(screen, GREEN, top_obstracle)
        pygame.draw.rect (screen, GREEN, bottom_obstracle)

    score_text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    clock.tick(30)
