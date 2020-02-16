import pygame

pygame.init()
window = pygame.display.set_mode((3000, 1000))
window.fill((255,255,255))

SHIP_WIDTH, SHIP_HEIGHT = 100, 100
BULLET_WIDTH, BULLET_HEIGHT = 10, 5
rect_x, rect_y = 100, 100

rect = pygame.Rect(rect_x, rect_y, 100, 100)
clock = pygame.time.Clock()

targets = []

bullets = []
# pygame.draw.rect(window, (100, 123, 121), rect)

is_game_running = True

while is_game_running:

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (100, 123, 121), (rect_x, rect_y, 100, 100))
    # window.blit(rect)
    for bullet in bullets:
        bullet.x += 10
        pygame.draw.rect(window, (255, 0, 0), bullet)
    # for




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        #     elif event.key == pygame.K_s:
        #         rect_y += 5
        #     elif event.key == pygame.K_a:
        #         rect_x -= 5
        #     elif event.key == pygame.K_d:
        #         rect_x += 5


    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        rect_y += 3
    elif keys[pygame.K_w]:
        rect_y -= 3
    elif keys[pygame.K_a]:
        rect_x -= 3
    elif keys[pygame.K_d]:
        rect_x += 3
    elif keys[pygame.K_f]:
        bullet_rect = pygame.Rect(rect_x + SHIP_WIDTH - BULLET_WIDTH, rect_y + SHIP_HEIGHT / 2, 10, 5)
        bullets.append(bullet_rect)




    clock.tick(120)