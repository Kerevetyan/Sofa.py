
import pygame
import random

pygame.init()

# Екран і налаштування
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Blue")
clock = pygame.time.Clock()

# Кольори
WHITE = (255, 255, 255)
BLUE = (66, 102, 245)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Завантаження зображень
cat_img = pygame.image.load("character.png")
cat_img = pygame.transform.scale(cat_img, (40, 40))
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Гравець
player = cat_img.get_rect()
start_pos = (50, 50)
player.topleft = start_pos
player_speed = 5

# Ціль
goal = pygame.Rect(WIDTH - 80, HEIGHT - 80, 30, 30)

# Таймер
font = pygame.font.SysFont(None, 36)
start_ticks = pygame.time.get_ticks()  # старт часу
elapsed_time = 0

# Генерація перешкод
def generate_obstacles(n=10):
    obstacles = []
    for _ in range(n):
        w, h = random.randint(30, 100), random.randint(30, 100)
        x, y = random.randint(0, WIDTH - w), random.randint(0, HEIGHT - h)
        rect = pygame.Rect(x, y, w, h)
        if rect.colliderect(player) or rect.colliderect(goal):
            continue
        obstacles.append(rect)
    return obstacles

obstacles = generate_obstacles()

# Меню після перемоги
def show_win_screen():
    win_text = pygame.font.SysFont(None, 60).render("Ти переміг!", True, GREEN)
    retry_text = font.render("Натисни R щоб спробувати ще", True, WHITE)
    time_text = font.render(f"Час: {elapsed_time:.1f} с", True, WHITE)

    screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - 100))
    screen.blit(time_text, (WIDTH//2 - time_text.get_width()//2, HEIGHT//2 - 40))
    screen.blit(retry_text, (WIDTH//2 - retry_text.get_width()//2, HEIGHT//2 + 20))

# Основна гра
running = True
game_won = False

while running:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_won:
        # Таймер у секундах
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

        # Рух гравця
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += player_speed

        # Зіткнення з перешкодами
        for obs in obstacles:
            if player.colliderect(obs):
                player.topleft = start_pos
                start_ticks = pygame.time.get_ticks()  # скидаємо таймер

        # Досягнення цілі
        if player.colliderect(goal):
            game_won = True

        # Малювання об'єктів
        for obs in obstacles:
            pygame.draw.rect(screen, BLUE, obs)
        pygame.draw.rect(screen, RED, goal)
        screen.blit(cat_img, player.topleft)

        # Вивід таймера
        time_text = font.render(f"Час: {elapsed_time:.1f} с", True, WHITE)
        screen.blit(time_text, (10, 10))

    else:
        show_win_screen()
        if keys[pygame.K_r]:  # Рестарт
            player.topleft = start_pos
            obstacles = generate_obstacles()
            game_won = False
            start_ticks = pygame.time.get_ticks()  # перезапуск таймера

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
