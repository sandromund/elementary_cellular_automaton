import sys

import pygame
import yaml
from src.Automat import Automat

CONFIG_FILE = "config.yaml"

with open(CONFIG_FILE) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

automat = Automat(config=config)
screen = pygame.display.set_mode((config.get("window_size"), config.get("window_size")))
pygame.display.set_caption(config.get("title"))

running = True
while running:
    screen.fill(tuple(config.get("background_color")))
    automat.draw(surface=screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
sys.exit()
