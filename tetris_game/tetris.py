import pygame
import utils as ut

class Game:
    def __init__(self):
        self.grid = [[0 for _ in range(ut.GRID_WIDTH)] for _ in range(ut.GRID_HEIGHT)]
        self.playing = True
        self.new_shape = True
        self.last_fall_time = pygame.time.get_ticks()
    
    def draw_grid(self, surface):
        for y in range(ut.GRID_HEIGHT):
            for x in range(ut.GRID_WIDTH):
                empty_cell = pygame.Rect(x * ut.GRID_SIZE, y * ut.GRID_SIZE, ut.GRID_SIZE, ut.GRID_SIZE)
                pygame.draw.rect(surface, ut.WHITE, empty_cell, 1)
    
    def draw(self, surface):
        self.draw_grid(surface)
        if self.new_shape:
            self.shape = ut.Shape()
        self.shape.draw_shape(surface)

    def shape_fall(self):
        now = pygame.time.get_ticks()
        if now - self.last_fall_time > 500:
            self.shape.y += 1
            self.last_fall_time = now

    def move_shape_left(self):
        self.shape.x -= 1

    def move_shape_right(self):
        self.shape.x += 1


def main():
    pygame.init()
    window = pygame.display.set_mode((ut.SCREEN_WIDTH, ut.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    game = Game()

    while game.playing:
        window.fill(ut.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_shape_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_shape_right()


        game.draw(window)
        game.new_shape = False
        game.shape_fall()
        pygame.display.flip()

if __name__ == "__main__":
    main()
