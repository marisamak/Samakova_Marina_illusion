import random
import pygame
from all_colors import COLORS

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Иллюзия")
screen.fill((255, 255, 255))

x, y = screen_width // 2, screen_height // 2
rect_size = 200
FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_size = rect_size
    for i in range(19):
        color = random.choice(COLORS)
        pygame.draw.rect(screen, color, (x - current_size // 2, y - current_size // 2, current_size, current_size))
        current_size -= 10

    pygame.display.flip()
    clock.tick(FPS)

# Завершение работы
pygame.quit()