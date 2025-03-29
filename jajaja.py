import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Рух об'єкта за допомогою Enter")
rect_position = pygame.math.Vector2(300, 200)
object_size = 100
object_color = (78, 3, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_position.x += 50
            elif event.key == pygame.K_LEFT:
                rect_position.x -= 50
            elif event.key == pygame.K_DOWN:
                rect_position.y += 50
            elif event.key == pygame.K_UP:
                rect_position.y -= 50
    screen.fill((0, 1, 5))
    pygame.draw.rect(screen, object_color, (rect_position.x, rect_position.y, object_size, object_size))
    pygame.display.flip()
pygame.quit()
