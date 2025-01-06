import pygame
import tetris
import utils as ut
import read

def menu():
	pygame.init()
	window = pygame.display.set_mode((600, 600))
	pygame.display.set_caption("Tetris Menu")
	clock = pygame.time.Clock()

	font = pygame.font.Font(None, 48)
	options = ["Play", "Quit"]
	selected = 0

	while True:
		window.fill(ut.BLACK)

		title_surface = font.render("TETRIS MENU", True, ut.WHITE)
		title_rect = title_surface.get_rect(center=(300, 150))
		window.blit(title_surface, title_rect)

		for i in range(len(options)):
			color = ut.WHITE if i == selected else ut.GREY
			option_surface = font.render(options[i], True, color)
			option_rect = option_surface.get_rect(center=(300, 300 + i * 50))
			window.blit(option_surface, option_rect)

		pygame.display.flip()

		x_dir, y_dir, pressed = read.parse_data()

		if y_dir == "up":
			selected = 0
		elif y_dir == "down":
			selected = 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if selected == 0:
						tetris.main()
					elif selected == 1:
						pygame.quit()
						return

		clock.tick(60)
