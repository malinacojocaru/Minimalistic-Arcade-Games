import pygame
import sys
import snake
import read

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHADOW = (100, 100, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

def draw_menu(selected_option):

    background = pygame.image.load("./utils/snake.png")
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

def main_menu():
    selected_option = "play"
    running = True
    
    while running:
        draw_menu(selected_option)
        
        x_dir, y_dir, pressed = read.parse_data()

        if y_dir == "up":
            selected_option = "play"
        elif y_dir == "down":
            selected_option = "quit"
        
        # if pressed:
        #     if selected_option == "play":
        #             snake.gameLoop()
        #     elif selected_option == "quit":
        #         running = False
        #         sys.exit()
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

#imi trebuie asta ca sa nu se execute direct la import in menu_all
if __name__ == "__main__":
    main_menu()
