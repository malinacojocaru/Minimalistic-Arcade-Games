import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        self.playing = True
    
    def draw_grid(self, surface):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(surface, WHITE, cell, 1)
    

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    game = Game()

    while game.playing:
        game.draw_grid(window)
        pygame.display.flip()

if __name__ == "__main__":
    main()
