"""All code for doing statiscal analysis on tweets."""
from data_formatting import Tweet
from typing import List, Dict, Tuple
from vader_analysis import range_of_compound_values, vader_values
import plotly.graph_objects as go
import matplotlib.pyplot as plt

import statistics


def frequency(tweets: List[Tweet]) -> Dict[str, int]:
    """Return the frequency of positive, negative and neutral tweets in the
    list of tweets provided."""
    news_neutral_tweets = [tweet for tweet in tweets if tweet.sentiment in {0,2}]
    range_compound = range_of_compound_values(news_neutral_tweets)
    tweets_values = [(tweet, vader_values(tweet, 'compound')) for tweet in tweets]
    freq_neg = 0
    freq_pos = 0
    freq_neu = 0
    for tweet_tuple in tweets_values:
        if tweet_tuple[1] < range_compound[0]:
            freq_neg += 1
        elif tweet_tuple[1] > range_compound[1]:
            freq_pos += 1
        elif range_compound[0] <= tweet_tuple[1] <= range_compound[1]:
            freq_neu += 1
    return {'positive': freq_pos, 'neutral': freq_neu, 'negative': freq_neg}


def normal_histogram(tweets: List[Tweet]) -> None:
    """Displays a normal histogram in plotly containing the
    compound values of each tweet in tweets.
    """
    compound_values = []
    for tweet in tweets:
        compound_values.append(vader_values(tweet, 'compound'))
    fig = go.Figure(data=[go.Histogram(x=compound_values, histnorm='probability')])
    fig.update_traces(xbins_size=0.01, selector=dict(type='histogram'))
    fig.show()


def summary(data: List[float]) -> Dict[str, int]:
    """Return a dictionary of summary statistics for a list of numbers.

    Mappings:
        - 'mean': mean of the data
        - 'median': median of the data
        - 'stdev': standard deviation of the data (assuming full dataset)
        - 'range': (statistical) range of the data
        - 'iqr': interquartile range of the data
    
    Preconditions:
        - len(data) > 0
    """
    return {
        'mean': statistics.mean(data),
        'median': statistics.median(data),
        'stdev': statistics.pstdev(data),
        'range': max(data) - min(data),
        'iqt': ...
    }


def plot_pos_neg(values: List[Tuple[float, float]]) -> None:
    """Given tuples of positive and negative values of a list of tweets,
    plots them in a 2D plane with the x-axis as positive values and the 
    y-axis representing negative values."""
    x_values = [negative[1] for negative in values]
    y_values = [positive[0] for positive in values]
    plt.scatter(x_values, y_values)
    plt.show()