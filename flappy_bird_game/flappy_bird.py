
import pygame
import random
import time
import read

from sys import exit

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 550, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("photos/background.png")
bird_upflap = pygame.image.load("photos/bird_up.png")
ground = pygame.image.load("photos/ground.png")
pipe_bottom = pygame.image.load("photos/pipe_bottom.png")
pipe_top = pygame.image.load("photos/pipe_top.png")
game_over = pygame.image.load("photos/game_over.png")


speed = 1;
score = 0
font = pygame.font.SysFont('comicsans', 26)
menu_font = pygame.font.SysFont('monospace', 40)

start_pos = (100,200)

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_upflap
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.alive = True
        self.velocity = 0

    def update(self, user_input):
        self.rect.y = self.rect.y + 1
        self.velocity = self.velocity + 0.5
        if self.velocity > 8:
            self.velocity = 8
        if self.rect.y < 500:
            self.rect.y = self.rect.y + self.velocity
        if user_input == True and self.rect.y > 50 and self.alive == True:
            self.velocity = -8
        self.image = pygame.transform.rotate(bird_upflap, -self.velocity * 4)


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x = self.rect.x - speed
        if self.rect.x <= -WIDTH:
            self.kill()

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pipe_type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.passed = False

    def update(self):
        self.rect.x = self.rect.x - speed
        if self.rect.x <= -WIDTH:
            self.kill()
        if start_pos[0] > self.rect.topright[0] and self.passed == False:
            self.passed = True
            global score
            score = score + 0.5

def main():
    x = 0
    y = 520
    timer = 0

    ground = pygame.sprite.Group()
    ground.add(Ground(x, y))

    global score
    score = 0

    pipes = pygame.sprite.Group()

    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    running = True
    while running:
        quit_game()
        window.fill((0, 0, 0))
        window.blit(background, (0, 0))

        x_dir, y_dir, pressed = read.parse_data()
        if pressed == True or y_dir == "up":
            user_input = True
        else:
            user_input = False

        clock.tick(60);

        if len(ground) < 2:
            ground.add(Ground(WIDTH, y))

        bird.draw(window)
        pipes.draw(window)
        ground.draw(window)

        text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
        window.blit(text, (20, 20))

        if bird.sprite.alive == True:
            ground.update()
            pipes.update()
        bird.update(user_input)

        collisions = pygame.sprite.spritecollide(bird.sprite, pipes, False)
        ground_collisions = pygame.sprite.spritecollide(bird.sprite, ground, False)

        if collisions or ground_collisions:
            bird.sprite.alive = False
            running = False
            window.blit(game_over, (160, 260))

        if timer <= 0 and bird.sprite.alive == True:
            x_top = 550
            x_bottom = 550
            y_top = random.randint(-650, -500)
            y_bottom = y_top + random.randint(130, 170) + pipe_bottom.get_height()
            pipes.add(Pipe(x_top, y_top, pipe_top))
            pipes.add(Pipe(x_bottom, y_bottom, pipe_bottom))
            timer = random.randint(200, 250)
        timer = timer - 1

        pygame.display.update()

    time.sleep(2)
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))

    text = menu_font.render(f"Menu", True, (16, 51, 23))
    window.blit(text, (225, 70))

    pygame.draw.rect(window, (16, 51, 23), pygame.Rect(125, 160, 300, 100), 2)
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 350, 300, 100), 2)
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 540, 300, 100), 2)

    text = menu_font.render(f"Play again", True, (0, 0, 0))
    window.blit(text, (155, 180))

    text = menu_font.render(f"Main menu", True, (0, 0, 0))
    window.blit(text, (160, 370))

    text = menu_font.render(f"Exit", True, (0, 0, 0))
    window.blit(text, (230, 560))

    pygame.display.update()

    button_pressed = False
    current = 1
    while button_pressed == False:
        quit_game()
        x_dir, y_dir, pressed = read.parse_data()

        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 160, 300, 100), 2)
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 350, 300, 100),  2)
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(125, 540, 300, 100),  2)
        
        if y_dir == "up":
            current = current - 1
            if current < 1:
                current = 3
            
        elif y_dir == "down":
            current = current + 1
            if current > 3:
                current = 1
            
        if current == 1:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(125, 160, 300, 100), 2)
            text = menu_font.render(f"Play again", True, (0, 0, 0))
            window.blit(text, (155, 180))
        elif current == 2:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(125, 350, 300, 100), 2)
            text = menu_font.render(f"Main menu", True, (0, 0, 0))
            window.blit(text, (160, 370))
        elif current == 3:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(125, 540, 300, 100), 2)
            text = menu_font.render(f"Exit", True, (0, 0, 0))
            window.blit(text, (230, 560))

        if pressed == True:
            button_pressed = True
            if current == 1:
                main()
            elif current == 2:
                main_menu()
            elif current == 3:
                pygame.quit()
                exit()
        time.sleep(0.1)

        pygame.display.update()

main()