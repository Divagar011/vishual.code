import pygame
import random
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display
display = (800, 600)
screen = pygame.display.set_mode(display)
pygame.display.set_caption("Crown Collection Game")

# Colors
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Player properties
player_size = 50
player_x = display[0] // 2 - player_size // 2
player_y = display[1] - player_size
player_speed = 5

# Crown properties
crown_size = 30
crown_count = 10
crowns = []

# Initialize the crowns
for _ in range(crown_count):
    crown_x = random.randint(0, display[0] - crown_size)
    crown_y = random.randint(0, display[1] - crown_size)
    crowns.append((crown_x, crown_y))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= player_speed
    if keys[K_RIGHT]:
        player_x += player_speed
    if keys[K_UP]:
        player_y -= player_speed
    if keys[K_DOWN]:
        player_y += player_speed

    # Clear the screen/
    screen.fill(white)

    # Draw the player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Draw the crowns
    for crown_x, crown_y in crowns:
        pygame.draw.rect(screen, yellow, (crown_x, crown_y, crown_size, crown_size))

    # Check for collision with crowns
    for crown in crowns[:]:
        crown_rect = pygame.Rect(crown[0], crown[1], crown_size, crown_size)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        if player_rect.colliderect(crown_rect):
            crowns.remove(crown)

    pygame.display.update()
