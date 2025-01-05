import pygame
import time
import random
import read
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
SHADOW = (100, 100, 100)

BLOCK_SIZE = 20
SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    #face din text o imagine ca sa poata sa apara in joc
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    #blit suprapune suprafetele pe pozitia 10,10
    screen.blit(value, [10, 10])

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

def win_menu(selected_option):
    continue_button = font_style.render("Continue", True, WHITE if selected_option == "continue" else SHADOW)
    continue_button_ = continue_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(continue_button, continue_button_)
    
    quit_button = font_style.render("Quit", True, WHITE if selected_option == "quit" else SHADOW)
    quit_button_ = quit_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(quit_button, quit_button_)

def lost_menu(selected_option):
    again_button = font_style.render("Play again", True, WHITE if selected_option == "again" else SHADOW)
    again_button_ = again_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(again_button, again_button_)
    
    quit_button = font_style.render("Quit", True, WHITE if selected_option == "quit" else SHADOW)
    quit_button_ = quit_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(quit_button, quit_button_)
    
def check(length_of_snake):
    if length_of_snake > 30:
        backgrd2 = pygame.image.load("./utils/happy_face.jpg")
        backgrd2 = pygame.transform.scale(backgrd2, (WIDTH, HEIGHT))
        screen.blit(backgrd2, (0,0))
        selected_option = "continue"

        pygame.display.update()

        while 1:
            win_menu(selected_option)
            x_dir, y_dir, pressed = read.parse_data()

            if y_dir == "up":
                selected_option = "continue"
            elif y_dir == "down":
                selected_option = "quit"
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if selected_option == "continue":
                            gameLoop()
                        elif selected_option == "quit":
                            sys.exit()
            pygame.display.flip()

def gameLoop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    #aliniem mancarea 
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    background = pygame.image.load("./utils/snake.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    while not game_over:

        while game_close:
            #dispare sarpele
            backgrd = pygame.image.load("./utils/sad_face.jpg")
            backgrd = pygame.transform.scale(backgrd, (WIDTH, HEIGHT))
            screen.blit(backgrd, (0,0))

            pygame.display.update()
            selected_option = "again"

            while 1:
                lost_menu(selected_option)
                x_dir, y_dir, pressed = read.parse_data()

                if y_dir == "up":
                    selected_option = "again"
                elif y_dir == "down":
                    selected_option = "quit"
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if selected_option == "again":
                                gameLoop()
                            elif selected_option == "quit":
                                sys.exit()
                pygame.display.flip()

        x_dir, y_dir, pressed = read.parse_data()

        if x_dir == "left":
            x_change = -BLOCK_SIZE
            y_change = 0
        elif x_dir == "right":
            x_change = BLOCK_SIZE
            y_change = 0
        elif y_dir == "up":
            y_change = -BLOCK_SIZE
            x_change = 0
        elif y_dir == "down":
            y_change = BLOCK_SIZE
            x_change = 0

        #daca s-a iesit din teren
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        #face ecranul si deseneaza mancarea
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, WHITE, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        #vedem daca nu cumva se atinge
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1
            check(length_of_snake)

        clock.tick(SPEED)

    pygame.quit()
    quit()
