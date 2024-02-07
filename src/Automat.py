import numpy as np
import pygame


class Automat:

    def __init__(self, config):
        self.tile_size = config.get("tile_size")
        self.n = config.get("window_size") // config.get("tile_size")
        self.cell_color = config.get("cell_color")

        self.data = np.zeros(shape=(self.n, self.n))

        self.data[0, self.n // 2] = 1
        print(self.data)

    def draw(self, surface):
        for i in range(self.n):
            for j in range(self.n):
                if self.data[i, j] > 0:
                    rect = (j * self.tile_size,
                            i * self.tile_size,
                            self.tile_size,
                            self.tile_size)
                    pygame.draw.rect(surface=surface,
                                     color=self.cell_color,
                                     rect=rect)
