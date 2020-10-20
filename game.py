import pygame
import time
import random
pygame.init()

# colors
black = 0, 0, 0
white = 255, 255, 255
sunset = 253, 72, 47
green = 0, 255, 0

# screen
width = 800
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (width, height))
bird_image = pygame.image.load('flappy_bird.png')
bird_image = pygame.transform.scale(bird_image, (100, 100))

# Score Function
def score(count):
    font = pygame.font.Font('font_1.ttf', 20)
    text = font.render("Score: " + str(count), True, white)
    screen.blit(text, [0, 0])

def blocks(x_block, y_block, block_width, block_height, gap, color):
    pygame.draw.rect(screen, color, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(screen, color, [x_block, y_block + block_height + int(gap), block_width, height])
 
def make_text_objects(text, font):
    text_surface = font.render(text, True, sunset)
    return text_surface, text_surface.get_rect()

def msg_surface(text):
    small_text = pygame.font.Font('font_1.ttf', 20)
    large_text = pygame.font.Font('font_1.ttf', 150)

    title_text_surface, title_text_rect = make_text_objects(text, large_text)
    title_text_rect.center = int(width / 2), int(height / 2)
    screen.blit(title_text_surface, title_text_rect)

    typ_text_surf, typ_text_rect = make_text_objects('Press any key to continue', small_text)
    typ_text_rect.center = int(width / 2), int(((height / 2) + 100))
    screen.blit(typ_text_surf, typ_text_rect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() is None:
        clock.tick()

    game()


def game_over():
    msg_surface('crashed!')


def bird(x, y, image):
    screen.blit(image, (x, y))


def game():
    x = 150
    y = 200
    y_move = 0

    x_block = width
    y_block = 0

    block_width = 75
    block_height = random.randint(0, (height / 2))
    gap = 50 * 3
    block_move = 4
    current_score = 0

    block_color = green

    game_cond = False

    while not game_cond:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                game_cond = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move
        screen.blit(background, (0, 0))
        # surface.fill(black)
        bird(x, y, bird_image)

        blocks(x_block, y_block, block_width, block_height, gap, block_color)
        score(current_score)
        x_block -= block_move

        if y > height or y < - 40:
            game_over()

        if x_block < (-1 * block_width):
            x_block = width
            block_height = random.randint(0, (height / 2))
            block_color = green
            current_score += 1

        if x + 23 > x_block:
            if x < x_block + block_width:
                if y < block_height - 25:
                    if x - 23 < block_width + x_block:
                        game_over()

        if x + 23 > x_block:
            if y + 10 > block_height - 50 + gap:
                if x < block_width + x_block:
                    game_over()


        pygame.display.update()
        clock.tick(60)


game()
