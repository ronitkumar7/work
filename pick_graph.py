"""Run a PyGame that allows the user to pick the graph they want to visualize."""

import pygame


def run_game() -> None:
    """Run the pygame"""

    pygame.init()

    width = 800
    height = 600

    screen = pygame.display.set_mode((width, height))

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    pygame.display.set_caption('Pick a Graph')

    font1 = pygame.font.Font('freesansbold.ttf', 36)
    title = font1.render('Welcome to our sentiment analysis!', True, black)
    title_rect = title.get_rect()
    title_rect.center = (width//2, 50)

    font2 = pygame.font.Font('freesansbold.ttf', 18)
    text1 = font2.render('Please choose the graph you would like to look at', True, black)
    text1_rect = text1.get_rect()
    text1_rect.center = (width // 2, 100)

    text2 = font2.render('Negative Tweets', True, black)
    text2_rect = text2.get_rect()
    text2_rect.center = (width // 4, 175)

    text3 = font2.render('Positive Tweets', True, black)
    text3_rect = text3.get_rect()
    text3_rect.center = (3 * width // 4, 175)

    text4 = font2.render('Neutral Tweets', True, black)
    text4_rect = text4.get_rect()
    text4_rect.center = (width // 4, 375)

    text5 = font2.render('News Tweets', True, black)
    text5_rect = text5.get_rect()
    text5_rect.center = (3 * width // 4, 375)

    running = True

    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                ...

        screen.fill(white)

        screen.blit(title, title_rect)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        screen.blit(text3, text3_rect)
        screen.blit(text4, text4_rect)
        screen.blit(text5, text5_rect)

        pygame.display.update()

    pygame.quit()
    quit()
