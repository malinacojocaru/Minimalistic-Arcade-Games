import pygame
import tetris
import utils as ut

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

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					selected = (selected - 1) % len(options)
				elif event.key == pygame.K_DOWN:
					selected = (selected + 1) % len(options)
				elif event.key == pygame.K_RETURN:
					if options[selected] == "Play":
						tetris.main()
					elif options[selected] == "Quit":
						pygame.quit()
						return
		clock.tick(60)
