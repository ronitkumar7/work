"""
CSC110 Project: Climate Change Sentiment on Twitter: Main

Module Description:
====================
The module contains the function calls to utilize our other modules to run our pygame application
and display the comparison of climate change sentiment on Twitter.
"""

import data_formatting
import pick_graph

if __name__ == "__main__":

    # Data formatting
    FILEPATH = 'twitter_sentiment_data.csv'

    dataset = data_formatting.process(FILEPATH)  # Processes the data into a list of tweets
    sorted_tweets = data_formatting.sort_tweets(dataset)
    # Sorts the list into a dictionary where possible opinion values map to tweets with those
    # opinion values

    # Runs the interactive pygame
    pick_graph.run_game(sorted_tweets)
