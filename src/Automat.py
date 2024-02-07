import numpy as np
import pygame


def rule_to_bin_array(rule: int) -> np.array:
    rule_bin = np.zeros(shape=(8,))
    for i, k in enumerate(reversed(str(bin(rule))[2:])):
        if k == "1":
            rule_bin[7 - i] = 1
    return rule_bin


class Automat:

    def __init__(self, config):
        self.tile_size = config.get("tile_size")
        self.n = config.get("window_size") // config.get("tile_size")
        self.cell_color = config.get("cell_color")
        self.data = np.zeros(shape=(self.n, self.n))
        self.data[0, self.n // 2] = 1
        self.rule = 57
        self.bin_rule = rule_to_bin_array(self.rule)
        self.current_row = 1

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

    def apply_rule_single_cell(self, i, j):
        if not (0 < i < self.n) or not (0 < j < self.n - 1):
            return
        left = self.data[i - 1][j - 1] > 0
        mid = self.data[i - 1][j] > 0
        right = self.data[i - 1][j + 1] > 0

        if left:
            if mid:
                if right:
                    self.data[i, j] = self.bin_rule[0]
                else:
                    self.data[i, j] = self.bin_rule[1]
            else:
                if right:
                    self.data[i, j] = self.bin_rule[2]
                else:
                    self.data[i, j] = self.bin_rule[3]
        else:
            if mid:
                if right:
                    self.data[i, j] = self.bin_rule[4]
                else:
                    self.data[i, j] = self.bin_rule[5]
            else:
                if right:
                    self.data[i, j] = self.bin_rule[6]
                else:
                    self.data[i, j] = self.bin_rule[7]

    def apply_rule_row(self):
        for j in range(self.n):
            self.apply_rule_single_cell(i=self.current_row, j=j)
        self.current_row += 1

        if self.current_row > self.n:
            self.new_rule()

    def new_rule(self):
        self.data = np.zeros(shape=(self.n, self.n))
        self.data[0, self.n // 2] = 1
        self.rule += 1
        if self.rule > 255:
            self.rule = 0
        self.bin_rule = rule_to_bin_array(self.rule)
        self.current_row = 1
