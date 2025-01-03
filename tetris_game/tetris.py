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
            self.block = ut.Shape()
        self.block.draw_shape(surface)

    def valid_pos(self, x = 0, y = 0) -> bool:
        for i in range(self.block.shape_height):
            for j in range(self.block.shape_width):
                if self.block.shape[i][j]:
                    new_x = self.block.x + j + x
                    new_y = self.block.y + i + y
                    if (
                        new_x < 0 or
                        new_x >= ut.GRID_WIDTH or
                        new_y >= ut.GRID_HEIGHT or
                        (new_y >= 0 and self.grid[new_y][new_x])
                    ):
                        return False
        return True

    def shape_fall(self):
        now = pygame.time.get_ticks()
        if now - self.last_fall_time > 500:
            if self.valid_pos(0, 1):
                self.block.y += 1
            self.last_fall_time = now

    def move_shape_left(self):
        if self.valid_pos(-1, 0):
            self.block.x -= 1

    def move_shape_right(self):
        if self.valid_pos(1, 0):
            self.block.x += 1

    def rotate(self):
        original_shape = self.block.shape
        self.block.rotate()
        if not self.valid_pos():
            self.block.shape_width, self.block.shape_height = self.block.shape_height, self.block.shape_width
            self.block.shape = original_shape




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
                elif event.key == pygame.K_UP:
                    game.rotate()

        game.shape_fall()
        game.draw(window)
        game.new_shape = False
        pygame.display.flip()

if __name__ == "__main__":
    main()
