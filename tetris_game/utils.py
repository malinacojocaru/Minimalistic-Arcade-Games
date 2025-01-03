import random
import pygame

SCREEN_WIDTH = 330
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SHAPE_COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
]

SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 1, 1]],

    [[1, 0, 0],
     [1, 1, 1]],

    [[0, 0, 1],
     [1, 1, 1]],
]

class Shape:
    def __init__(self):
        self.color = random.choice(SHAPE_COLORS)
        self.shape = random.choice(SHAPES)
        self.shape_width = len(self.shape[0])
        self.shape_height = len(self.shape)
        self.x = (GRID_WIDTH - self.shape_width) // 2
        self.y = 0

    def draw_shape(self, surface):
        for i in range(self.shape_height):
            for j in range(self.shape_width):
                if self.shape[i][j]:
                    colored_cell = pygame.Rect((self.x + j) * GRID_SIZE,
                                               (self.y + i) * GRID_SIZE,
                                               GRID_SIZE,
                                               GRID_SIZE)
                    pygame.draw.rect(surface, self.color, colored_cell)

    def rotate(self):
        reversed_shape = self.shape[::-1]
        transposed_shape = zip(*reversed_shape)
        new_shape = [list(row) for row in transposed_shape]
        self.shape = new_shape
        self.shape_width, self.shape_height = self.shape_height, self.shape_width
