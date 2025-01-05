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

    pygame.draw.rect(window, (16, 51, 23), pygame.Rect(125, 160, 300, 100), 2)
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 540, 300, 100), 2)

    text = menu_font.render(f"Play", True, (0, 0, 0))
    window.blit(text, (155, 180))

    text = menu_font.render(f"Exit", True, (0, 0, 0))
    window.blit(text, (230, 560))

    pygame.display.update()

    current = 1
    button_pressed = False

    while not button_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current -= 1
                    if current < 1:
                        current = 2
                elif event.key == pygame.K_DOWN:
                    current += 1
                    if current > 2:
                        current = 1
                elif event.key == pygame.K_RETURN:
                    button_pressed = True
                    
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 160, 300, 100), 2)
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 540, 300, 100), 2)

        if current == 1:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(125, 160, 300, 100), 2)
            text = menu_font.render(f"Play", True, (0, 0, 0))
            window.blit(text, (155, 180))
        elif current == 2:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(125, 540, 300, 100), 2)
            text = menu_font.render(f"Exit", True, (0, 0, 0))
            window.blit(text, (230, 560))

        pygame.display.update()

    if current == 1:
        flappy_bird.flappy_main()
    elif current == 2:
        pygame.quit()
        exit()


if __name__ == "__main__":
    flappy_menu()
