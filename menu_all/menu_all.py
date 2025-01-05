import pygame
import sys
import os
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), "../snake_game")))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../snake_game")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../tetris_game")))
import snake
import snake_menu
import read
import tetris_menu

#trebuie rulat cu asta python -m Minimalistic-Arcade-Games.menu_all.menu_all

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHADOW = (100, 100, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

def draw_menu_games(selected_option):

    background = pygame.image.load("./Minimalistic-Arcade-Games/menu_all/utils/menu_all_pic.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0,0))
    
    font_style = pygame.font.Font(None, 35)
    
    title_surface = font_style.render("Minimalistic Arcade Games", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)
    
    snake_game = font_style.render("Snake", True, BLACK if selected_option == "snake" else SHADOW)
    snake_game_ = snake_game.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25))
    screen.blit(snake_game, snake_game_)
    
    flappy_bird_game = font_style.render("Flappy Bird", True, BLACK if selected_option == "flappy_bird" else SHADOW)
    flappy_bird_game_ = flappy_bird_game.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25))
    screen.blit(flappy_bird_game, flappy_bird_game_)

    tetris_game = font_style.render("Tetris", True, BLACK if selected_option == "tetris" else SHADOW)
    tetris_game_ = tetris_game.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75))
    screen.blit(tetris_game, tetris_game_)

def menu_games():
    selected_option = "snake"
    running = True
    
    while running:
        draw_menu_games(selected_option)
        
        x_dir, y_dir, pressed = read.parse_data()

        if y_dir == "up":
            if selected_option == "flappy_bird":
                selected_option = "snake"
            elif selected_option == "tetris":
                selected_option = "flappy_bird"

        if y_dir == "down":
            if selected_option == "flappy_bird":
                selected_option = "tetris"
            elif selected_option == "snake":
                selected_option = "flappy_bird"
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selected_option == "snake":
                        snake_menu.main_menu()
                    elif selected_option == "tetris":
                        tetris_menu.menu()

            # elif selected_option == "flappy_bird":
            #     #jocul de flappy
            #     snake.gameLoop()
            # elif selected_option == "tetris":
            #     #jocul de tetris
            #     snake.gameLoop()
             
        pygame.display.flip()

if __name__ == "__main__":
    menu_games()