import pygame
import utils as ut

class Game:
    def __init__(self):
        self.grid = [[0 for _ in range(ut.GRID_WIDTH)] for _ in range(ut.GRID_HEIGHT)]
        self.playing = True
        self.new_shape = True
        self.fast_fall = False
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
        for i in range(ut.GRID_HEIGHT):
            for j in range(ut.GRID_WIDTH):
                if self.grid[i][j]:
                    colored_cell = pygame.Rect(j * ut.GRID_SIZE,
                                               i * ut.GRID_SIZE,
                                               ut.GRID_SIZE,
                                               ut.GRID_SIZE)
                    pygame.draw.rect(surface, self.grid[i][j], colored_cell)

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

    def lock_blocks(self):
        for i in range(self.block.shape_height):
            for j in range(self.block.shape_width):
                if self.block.shape[i][j]:
                    self.grid[self.block.y + i][self.block.x + j] = self.block.color
                    if self.block.y + i == 0:
                        self.playing = False
        self.clear_lines()

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        while len(new_grid) < ut.GRID_HEIGHT:
            new_grid.insert(0, [0 for _ in range(ut.GRID_WIDTH)])
        self.grid = new_grid

    def shape_fall(self):
        now = pygame.time.get_ticks()
        interval = 100 if self.fast_fall else 500
        if now - self.last_fall_time > interval:
            if self.valid_pos(0, 1):
                self.block.y += 1
            else:
                self.new_shape = True
                self.lock_blocks()
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
    def game_over(self, window):
        window.fill(ut.BLACK)
        with open("/home/alex/Facultate/Ia4/Minimalistic-Arcade-Games/tetris_game/game_over.txt", "r") as file:
            lines = file.readlines()
    
        font = pygame.font.Font(None, 24)
        x = ut.SCREEN_WIDTH // 2
        y_offset = ut.SCREEN_HEIGHT // 2
        for line in lines:
            text_surface = font.render(line.rstrip(), True, ut.WHITE)
            window.blit(text_surface, (x, y_offset))
            y_offset += font.get_linesize()
        pygame.display.flip()





def main():
    pygame.init()
    window = pygame.display.set_mode((ut.SCREEN_WIDTH, ut.SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    game = Game()
    clock = pygame.time.Clock()
    lost = True

    while game.playing:
        window.fill(ut.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                lost = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_shape_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_shape_right()
                elif event.key == pygame.K_UP:
                    game.rotate()
                elif event.key == pygame.K_DOWN:
                    game.fast_fall = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    game.fast_fall = False

        game.shape_fall()
        game.draw(window)
        game.new_shape = False
        pygame.display.flip()
        clock.tick(30)
    
    if lost:
        game.game_over(window)
        pygame.time.wait(1000)

if __name__ == "__main__":
    main()
