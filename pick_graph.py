"""Run a PyGame that allows the user to pick the graph they want to visualize."""

import pygame
import stats_analysis
from vader_analysis import add_vader_to_tweets
from data_formatting import Tweet
from typing import List, Dict


def run_game(tweets: Dict[int, List[Tweet]]) -> None:
    """Run the pygame"""

    neg_tweets = tweets[-1]
    add_vader_to_tweets(neg_tweets)
    neut_tweets = tweets[0]
    add_vader_to_tweets(neut_tweets)
    pos_tweets = tweets[1]
    add_vader_to_tweets(pos_tweets)
    news_tweets = tweets[2]
    add_vader_to_tweets(news_tweets)

    pygame.init()

    width = 800
    height = 600

    screen = pygame.display.set_mode((width, height))

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    dark_red = (200, 0, 0)
    green = (0, 200, 0)
    dark_green = (50, 150, 0)
    blue = (0, 0, 255)
    dark_blue = (0, 0, 200)
    yellow = (255, 233, 0)
    dark_yellow = (246, 190, 0)
    purple = (128, 0, 128)
    dark_purple = (96, 0, 128)

    pygame.display.set_caption('Pick a Graph')

    # Create text
    font1 = pygame.font.Font('freesansbold.ttf', 36)
    title = font1.render('Welcome to our sentiment analysis!', True, black)
    title_rect = title.get_rect()
    title_rect.center = (width//2, 50)

    font2 = pygame.font.Font('freesansbold.ttf', 18)
    text1 = font2.render('Please click on the graph you would like to look at', True, black)
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

    but_text1 = font2.render('Frequency Histogram', True, white)
    but_text1_rect = but_text1.get_rect()

    but_text2 = font2.render('Pos-Neg Graph', True, white)
    but_text2_rect = but_text2.get_rect()

    but_text3 = font2.render('Comparison', True, white)
    but_text3_rect = but_text3.get_rect()

    font3 = pygame.font.Font('freesansbold.ttf', 12)
    note_text1 = font3.render('* Frequency histogram plots the distribution '
                              'of intervals of compound vader values for'
                              ' a given list of tweets', True, black)
    note_text1_rect = note_text1.get_rect()
    note_text1_rect.center = (width // 2, height - 50)

    note_text2 = font3.render('* Pos-neg graphs the spread of positive vader '
                              'values (on the x-axis) verses negative '
                              'vader values (on the y-axis)', True, black)
    note_text2_rect = note_text2.get_rect()
    note_text2_rect.center = (width // 2, height - 25)

    def mouse_in(x_pos: int, y_pos: int) -> bool:
        """
        Check if the position of the mouse is inside a 200 by 50 rectangle
        with starting coordinates x_pos and y_pos
        """
        return x_pos < mouse[0] < x_pos + 200 and y_pos < mouse[1] < y_pos + 50

    running = True

    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

            # Add button functionality
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in(width // 8, 200):
                    stats_analysis.normal_histogram(neg_tweets)
                elif mouse_in(width // 8, 250):
                    stats_analysis.plot_pos_neg(neg_tweets)
                elif mouse_in(5 * width // 8, 200):
                    stats_analysis.normal_histogram(pos_tweets)
                elif mouse_in(5 * width // 8, 250):
                    stats_analysis.plot_pos_neg(pos_tweets)
                elif mouse_in(width // 8, 400):
                    stats_analysis.normal_histogram(neut_tweets)
                elif mouse_in(width // 8, 450):
                    stats_analysis.plot_pos_neg(neut_tweets)
                elif mouse_in(5 * width // 8, 400):
                    stats_analysis.normal_histogram(news_tweets)
                elif mouse_in(5 * width // 8, 450):
                    stats_analysis.plot_pos_neg(news_tweets)
                elif mouse_in(3 * width // 8, 325):
                    stats_analysis.plot_compound(tweets)

        screen.fill(white)

        # Add text to screen
        screen.blit(title, title_rect)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        screen.blit(text3, text3_rect)
        screen.blit(text4, text4_rect)
        screen.blit(text5, text5_rect)
        screen.blit(note_text1, note_text1_rect)
        screen.blit(note_text2, note_text2_rect)

        mouse = pygame.mouse.get_pos()

        # Add buttons to screen
        # Histogram for negative tweets
        if mouse_in(width // 8, 200):
            pygame.draw.rect(screen, dark_red, (width // 8, 200, 200, 50))
            but_text1_rect.center = (width // 4, 225)
            screen.blit(but_text1, but_text1_rect)
        else:
            pygame.draw.rect(screen, red, (width // 8, 200, 200, 50))

        # Positive negative plot for negative tweets
        if mouse_in(width // 8, 250):
            pygame.draw.rect(screen, dark_red, (width // 8, 250, 200, 50))
            but_text2_rect.center = (width // 4, 275)
            screen.blit(but_text2, but_text2_rect)
        else:
            pygame.draw.rect(screen, red, (width // 8, 250, 200, 50))

        # Histogram for positive tweets
        if mouse_in(5 * width // 8, 200):
            pygame.draw.rect(screen, dark_green, (5 * width // 8, 200, 200, 50))
            but_text1_rect.center = (3 * width // 4, 225)
            screen.blit(but_text1, but_text1_rect)
        else:
            pygame.draw.rect(screen, green, (5 * width // 8, 200, 200, 50))

        # Positive negative plot for positive tweets
        if mouse_in(5 * width // 8, 250):
            pygame.draw.rect(screen, dark_green, (5 * width // 8, 250, 200, 50))
            but_text2_rect.center = (3 * width // 4, 275)
            screen.blit(but_text2, but_text2_rect)
        else:
            pygame.draw.rect(screen, green, (5 * width // 8, 250, 200, 50))

        # Histogram for neutral tweets
        if mouse_in(width // 8, 400):
            pygame.draw.rect(screen, dark_blue, (width // 8, 400, 200, 50))
            but_text1_rect.center = (width // 4, 425)
            screen.blit(but_text1, but_text1_rect)
        else:
            pygame.draw.rect(screen, blue, (width // 8, 400, 200, 50))

        # Positive negative plot for neutral tweets
        if mouse_in(width // 8, 450):
            pygame.draw.rect(screen, dark_blue, (width // 8, 450, 200, 50))
            but_text2_rect.center = (width // 4, 475)
            screen.blit(but_text2, but_text2_rect)
        else:
            pygame.draw.rect(screen, blue, (width // 8, 450, 200, 50))

        # Histogram for news related tweets
        if mouse_in(5 * width // 8, 400):
            pygame.draw.rect(screen, dark_yellow, (5 * width // 8, 400, 200, 50))
            but_text1_rect.center = (3 * width // 4, 425)
            screen.blit(but_text1, but_text1_rect)
        else:
            pygame.draw.rect(screen, yellow, (5 * width // 8, 400, 200, 50))

        # Positive negative plot for news related tweets
        if mouse_in(5 * width // 8, 450):
            pygame.draw.rect(screen, dark_yellow, (5 * width // 8, 450, 200, 50))
            but_text2_rect.center = (3 * width // 4, 475)
            screen.blit(but_text2, but_text2_rect)
        else:
            pygame.draw.rect(screen, yellow, (5 * width // 8, 450, 200, 50))

        # Comparison plot for all tweets
        if mouse_in(3 * width // 8, 325):
            pygame.draw.rect(screen, dark_purple, (3 * width // 8, 325, 200, 50))
            but_text3_rect.center = (width // 2, 350)
            screen.blit(but_text3, but_text3_rect)
        else:
            pygame.draw.rect(screen, purple, (3 * width // 8, 325, 200, 50))

        pygame.display.update()

    pygame.quit()
    quit()
