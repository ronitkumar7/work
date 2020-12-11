"""
Driver file for the Climate Change Sentiment on Twitter project.
"""

import data_formatting
import stats_analysis
import pick_graph

if __name__ == "__main__":

    # Data formatting
    FILEPATH = 'twitter_sentiment_data.csv'

    dataset = data_formatting.process(FILEPATH)
    sorted_tweets = data_formatting.sort_tweets(dataset)
    neg_tweets = sorted_tweets[-1]
    neut_tweets = sorted_tweets[0]
    pos_tweets = sorted_tweets[1]
    news_tweets = sorted_tweets[2]

    # Interactive pygame
    #
    # Create window and run interactive module
    pick_graph.run_game()

    # Statistical analysis
    #
    # Call any functions related to statistical analysis
    def graph_neg() -> None:
        """Graph negative tweets"""
        stats_analysis.normal_histogram(neg_tweets)


    def graph_pos() -> None:
        """Graph positive tweets"""
        stats_analysis.normal_histogram(neg_tweets)


    def graph_neut() -> None:
        """Graph neutral tweets"""
        stats_analysis.normal_histogram(neg_tweets)


    def graph_news() -> None:
        """Graph news tweets"""
        stats_analysis.normal_histogram(neg_tweets)
