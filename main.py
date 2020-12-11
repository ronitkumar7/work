"""
Driver file for the Climate Change Sentiment on Twitter project.
"""

import data_formatting
import pick_graph

if __name__ == "__main__":

    # Data formatting
    FILEPATH = 'twitter_sentiment_data.csv'

    dataset = data_formatting.process(FILEPATH)
    sorted_tweets = data_formatting.sort_tweets(dataset)

    # Interactive pygame
    pick_graph.run_game(sorted_tweets)
