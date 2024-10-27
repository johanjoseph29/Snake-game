import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

# Game dimensions
width, height = 600, 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

snake_speed = 15
snake_size = 10

# Fonts
message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def rungame():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10

    while not game_over:
        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render('GAME OVER', True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        rungame()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed
        game_display.fill(black)

        # Draw the target
        pygame.draw.rect(game_display, red, [target_x, target_y, snake_size, snake_size])
        
        # Update snake pixels
        snake_pixels.append((x, y))
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        # Draw the snake
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        # Check if snake has eaten the target
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10
            snake_length += 1

        # Check for self-collision
        if (x, y) in snake_pixels[:-1]:
            game_close = True

        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

rungame()

