import pygame
import random
import utils as ut

class Shape:
    def __init__(self):
        self.color = random.choice(ut.SHAPE_COLORS)
        self.shape = random.choice(ut.SHAPES)
        self.shape_width = len(self.shape[0])
        self.shape_height = len(self.shape)
        self.x = (ut.GRID_WIDTH - self.shape_width) // 2
        self.y = 0

    def draw_shape(self, surface):
        for i in range(self.shape_height):
            for j in range(self.shape_width):
                if self.shape[i][j]:
                    colored_cell = pygame.Rect((self.x + i) * ut.GRID_SIZE, (self.y + j) * ut.GRID_SIZE, ut.GRID_SIZE, ut.GRID_SIZE)
                    pygame.draw.rect(surface, self.color, colored_cell)

class Game:
    def __init__(self):
        self.grid = [[0 for _ in range(ut.GRID_WIDTH)] for _ in range(ut.GRID_HEIGHT)]
        self.playing = True
    
    def draw_grid(self, surface):
        for y in range(ut.GRID_HEIGHT):
            for x in range(ut.GRID_WIDTH):
                empty_cell = pygame.Rect(x * ut.GRID_SIZE, y * ut.GRID_SIZE, ut.GRID_SIZE, ut.GRID_SIZE)
                pygame.draw.rect(surface, ut.WHITE, empty_cell, 1)
    
    def draw(self, surface):
        self.draw_grid(surface)
        shape = Shape()
        shape.draw_shape(surface)

def main():
    pygame.init()
    window = pygame.display.set_mode((ut.SCREEN_WIDTH, ut.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    game = Game()

    test_draw = True

    while game.playing:
        #window.fill(ut.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False

        if test_draw:
            game.draw(window)
        test_draw = False
        pygame.display.flip()

if __name__ == "__main__":
    main()
