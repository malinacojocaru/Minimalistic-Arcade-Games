import pygame
import sys
import snake
import read as rd
import os



WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHADOW = (100, 100, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

def draw_menu(selected_option):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    background_path = os.path.join(script_dir, "utils/snake.png")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0,0))
    
    font_style = pygame.font.Font(None, 35)
    
    title_surface = font_style.render("Snake Game", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)
    
    play_surface = font_style.render("Play", True, WHITE if selected_option == "play" else SHADOW)
    play_rect = play_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(play_surface, play_rect)
    
    quit_surface = font_style.render("Quit", True, WHITE if selected_option == "quit" else SHADOW)
    quit_rect = quit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(quit_surface, quit_rect)

def snake_menu():
    selected_option = "play"
    running = True
    
    while running:
        draw_menu(selected_option)
        
        _, y_dir, _ = rd.parse_data()

        if y_dir == "up":
            selected_option = "play"
        elif y_dir == "down":
            selected_option = "quit"
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selected_option == "play":
                            snake.gameLoop()
                    elif selected_option == "quit":
                        running = False
                        sys.exit()
        
        pygame.display.flip()

if __name__ == "__main__":
    snake_menu()
