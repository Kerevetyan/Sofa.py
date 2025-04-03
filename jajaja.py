import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
WHITE = (140, 153, 250)
PURPLE = (118, 44, 245)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30
circle_color = PURPLE
font = pygame.font.SysFont("Arial", 30)
start_time = pygame.time.get_ticks()
last_move_time = 0
MOVE_INTERVAL = 888
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - x)**2 + (mouse_y - y)**2)**0.5
            
            if event.button == 1:
                circle_color = BLUE
                if distance <= RADIUS:
                    score += 1
                    print("Є влучання!")
            elif event.button == 2:
                circle_color = GREEN
                if distance <= RADIUS:
                    score += 1
                    print("Є влучання!")
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= MOVE_INTERVAL:
        x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        last_move_time = current_time
        circle_color = PURPLE

    screen.fill(WHITE)
    pygame.draw.circle(screen, circle_color, (x, y), RADIUS)
    score_text = font.render(f"Влучань: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    elapsed_time = (current_time - start_time)//1000
    time_text = font.render(f"Час: {elapsed_time} c", True, (0, 0, 0))
    screen.blit(time_text, (10, 40))
    pygame.draw.rect(screen, (88, 181, 252), (0, 0, 500, 500), 10)
    pygame.display.flip()
pygame.quit()
