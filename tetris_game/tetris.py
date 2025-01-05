import pygame
import utils as ut
import read as rd

class Game:
	def __init__(self):
		self.grid = [[0 for _ in range(ut.GRID_WIDTH)] for _ in range(ut.GRID_HEIGHT)]
		self.playing = True
		self.new_shape = True
		self.fast_fall = False
		self.last_fall_time = pygame.time.get_ticks()
		self.score = 0
		self.level = 1
		self.lines_cleared = 0
	
	def draw_info_panel(self, surface):
		font = pygame.font.Font(None, 36)
		x_start = ut.GAME_WIDTH + 20
		y_start = 50

		score_text = font.render(f"Score: {self.score}", True, ut.WHITE)
		surface.blit(score_text, (x_start, y_start))

		level_text = font.render(f"Level: {self.level}", True, ut.WHITE)
		surface.blit(level_text, (x_start, y_start + 40))

		lines_text = font.render(f"Lines: {self.lines_cleared}", True, ut.WHITE)
		surface.blit(lines_text, (x_start, y_start + 80))

	def draw_grid(self, surface):
		for y in range(ut.GRID_HEIGHT):
			for x in range(ut.GRID_WIDTH):
				empty_cell = pygame.Rect(x * ut.GRID_SIZE, y * ut.GRID_SIZE, ut.GRID_SIZE, ut.GRID_SIZE)
				pygame.draw.rect(surface, ut.WHITE, empty_cell, 1)
	
	def draw(self, surface):
		self.draw_grid(surface)
		self.block.draw_shape(surface)
		for i in range(ut.GRID_HEIGHT):
			for j in range(ut.GRID_WIDTH):
				if self.grid[i][j]:
					colored_cell = pygame.Rect(j * ut.GRID_SIZE,
											   i * ut.GRID_SIZE,
											   ut.GRID_SIZE,
											   ut.GRID_SIZE)
					pygame.draw.rect(surface, self.grid[i][j], colored_cell)
		self.draw_info_panel(surface)
		pygame.display.flip()
		

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
		cleared = len(self.grid) - len(new_grid)
		self.lines_cleared += cleared
		self.score += cleared * 100
		if self.lines_cleared // 10 > self.level - 1:
			self.level += 1
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
		font = pygame.font.Font("./Minimalistic-Arcade-Games/tetris_game/assets/CourierPrime-Bold.ttf", 15)

		start_x = ut.SCREEN_WIDTH // 4 - 70
		start_y = ut.SCREEN_HEIGHT // 2 - 70
		spacing = 20

		with open("./Minimalistic-Arcade-Games/tetris_game/assets/game_over.txt", "r") as file:
			lines = file.readlines()

		i = 0
		for line in lines:
			if line.endswith("\n"):
				line = line[:-1] 
			text_surface = font.render(line, True, ut.RED)
			text_rect = text_surface.get_rect(left=start_x, top=start_y + i * spacing)
			window.blit(text_surface, text_rect)
			i += 1

		pygame.display.flip()

def main():
	pygame.init()
	window = pygame.display.set_mode((ut.SCREEN_WIDTH, ut.SCREEN_HEIGHT))
	pygame.display.set_caption("Tetris")
	game = Game()
	clock = pygame.time.Clock()
	lost = True
	(old_x, old_y) = ('center', 'center')

	while game.playing:
		window.fill(ut.BLACK)
		if game.new_shape:
			game.block = ut.Shape()
			game.new_shape = False

		x, y, _ = rd.parse_data()
		if y == 'up':
			if old_y == y:
				y = 'center'
			else:
				old_y = y
		else:
			old_y = 'center'

		if x != 'center':
			if old_x == x:
				x = 'center'
			else:
				old_x = x
		else:
			old_x = 'center'

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.playing = False
				lost = False

		if x == 'left':
			game.move_shape_left()
		if x == 'right':
			game.move_shape_right()
			x = 'center'
		if y == 'up':
			game.rotate()
		if y == 'down':
			game.fast_fall = True
		if y == 'center':
			game.fast_fall = False
			# elif event.type == pygame.KEYDOWN:
			# 	if event.key == pygame.K_LEFT:
			# 		game.move_shape_left()
			# 	elif event.key == pygame.K_RIGHT:
			# 		game.move_shape_right()
			# 	elif event.key == pygame.K_UP:
			# 		game.rotate()
			# 	elif event.key == pygame.K_DOWN:
			# 		game.fast_fall = True
			# 	elif event.key == pygame.K_RETURN:
			# 		return
			# elif event.type == pygame.KEYUP:
			# 	if event.key == pygame.K_DOWN:
			# 		game.fast_fall = False

		game.shape_fall()
		game.draw(window)
		clock.tick(60)
	
	if lost:
		game.game_over(window)
		pygame.time.wait(2000)

if __name__ == "__main__":
	import tetris_menu
	tetris_menu.menu()
