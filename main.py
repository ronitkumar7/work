"""
Driver file for the Climate Change Sentiment on Twitter project.
"""

import data_formatting
import vader_analysis
import stats_analysis

if __name__ == "__main__":

    # Data formatting
    FILEPATH = 'twitter_sentiment_data.csv'

    dataset = data_formatting.process(FILEPATH)
    sorted_tweets = data_formatting.sort_tweets(dataset)
    neg_tweets = sorted_tweets[-1]
    neut_tweets = sorted_tweets[0]
    pos_tweets = sorted_tweets[1]
    news_tweets = sorted_tweets[2]

    # VADER sentiment analysis
    vader_analysis.analyze(dataset)

    # Statistical analysis
    #
    # Call any functions related to statistical analysis
    ...

    # Interactive pygame
    #
    # Create window and run interactive module
    ...