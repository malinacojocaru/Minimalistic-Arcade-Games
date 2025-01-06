import pygame
import time
from sys import exit
import flappy_bird


font = pygame.font.SysFont('comicsans', 26)
menu_font = pygame.font.SysFont('monospace', 40)

background = pygame.image.load("./Minimalistic-Arcade-Games/flappy_bird_game/utils/background.png")
bird_upflap = pygame.image.load("./Minimalistic-Arcade-Games/flappy_bird_game/utils/bird_up.png")
ground = pygame.image.load("./Minimalistic-Arcade-Games/flappy_bird_game/utils/ground.png")
pipe_bottom = pygame.image.load("./Minimalistic-Arcade-Games/flappy_bird_game/utils/pipe_bottom.png")
pipe_top = pygame.image.load("./Minimalistic-Arcade-Games/flappy_bird_game/utils/pipe_top.png")
game_over = pygame.image.load("./Minimalistic-Arcade-Games/flappy_bird_game/utils/game_over.png")


def flappy_menu():
    pygame.init()
    WIDTH, HEIGHT = 550, 720
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))

    text = menu_font.render(f"Menu", True, (16, 51, 23))
    window.blit(text, (225, 70))

    pygame.draw.rect(window, (16, 51, 23), pygame.Rect(125, 200, 300, 100), 2)
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 400, 300, 100), 2)

    text = menu_font.render(f"Play", True, (0, 0, 0))
    window.blit(text, (220, 220))

    text = menu_font.render(f"Exit", True, (0, 0, 0))
    window.blit(text, (230, 420))

    pygame.display.update()

    current = 1

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    current = 2
                elif event.key == pygame.K_UP:
                    current = 1
                elif event.key == pygame.K_RETURN:
                    if current == 1:
                        flappy_bird.flappy_main()
                        window = pygame.display.set_mode((WIDTH, HEIGHT))
                        window.fill((0, 0, 0))
                        window.blit(background, (0, 0))

                        text = menu_font.render(f"Menu", True, (16, 51, 23))
                        window.blit(text, (225, 70))

                        pygame.draw.rect(window, (16, 51, 23), pygame.Rect(125, 200, 300, 100), 2)
                        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 400, 300, 100), 2)

                        text = menu_font.render(f"Play", True, (0, 0, 0))
                        window.blit(text, (220, 220))

                        text = menu_font.render(f"Exit", True, (0, 0, 0))
                        window.blit(text, (230, 420))

                        pygame.display.update()
                    elif current == 2:
                        pygame.quit()
                        exit()
                    
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 200, 300, 100), 2)
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 400, 300, 100), 2)

        if current == 1:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(125, 200, 300, 100), 2)
            text = menu_font.render(f"Play", True, (0, 0, 0))
            window.blit(text, (220, 220))
        elif current == 2:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(125, 400, 300, 100), 2)
            text = menu_font.render(f"Exit", True, (0, 0, 0))
            window.blit(text, (230, 420))

        pygame.display.update()


if __name__ == "__main__":
    flappy_menu()
