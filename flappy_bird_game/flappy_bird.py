import pygame
import random
import time
import read_flappy as rd
import os

from sys import exit

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 550, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

script_dir = os.path.dirname(os.path.abspath(__file__))
background = pygame.image.load(os.path.join(script_dir, "utils/background.png"))
bird_upflap = pygame.image.load(os.path.join(script_dir, "utils/bird_up.png"))
ground = pygame.image.load(os.path.join(script_dir, "utils/ground.png"))
pipe_bottom = pygame.image.load(os.path.join(script_dir, "utils/pipe_bottom.png"))
pipe_top = pygame.image.load(os.path.join(script_dir, "utils/pipe_top.png"))
game_over = pygame.image.load(os.path.join(script_dir, "utils/game_over.png"))


speed = 1
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

def flappy_main():
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
        user_input = False

        y_dir = rd.parse_data()
        if y_dir < 400:
            user_input = True
        else:
            user_input = False

        clock.tick(60)

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
            pygame.display.update()
            time.sleep(1)
            window.fill((0,0,0))
            window.blit(background, (0,0))

        if timer <= 0 and bird.sprite.alive == True:
            x_top = 550
            x_bottom = 550
            y_top = random.randint(-650, -500)
            y_bottom = y_top + random.randint(170, 220) + pipe_bottom.get_height()
            pipes.add(Pipe(x_top, y_top, pipe_top))
            pipes.add(Pipe(x_bottom, y_bottom, pipe_bottom))
            timer = random.randint(200, 250)
        timer = timer - 1

        pygame.display.update()

if __name__ == "__main__":
    flappy_main()