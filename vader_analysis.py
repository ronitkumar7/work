"""
Credit for vaderSentiment:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List, Tuple
from data_formatting import Tweet


def add_vader_to_tweets(tweets: List[Tweet]) -> None:
    """Returns the positive, negative, neutral or compound value of a tweet as 
    calculated by the polarity_scores method of SentimentIntensityAnalyzer(). 
    
    Preconditions: 
        - value in {'neg', 'neu', 'pos', 'compound'}
    """
    analyzer = SentimentIntensityAnalyzer()
    for tweet in tweets:
        tweet.vader = analyzer.polarity_scores(tweet.content)


def range_of_compound_values(tweets: List[Tweet]) -> Tuple[float, float]:
    """Returns the range of compound values of a list of given tweets in the 
    form of a tuple (min, max) where min is the lowest compound value and max 
    is the highest compound value. 
    
    Preconditions:
        - tweets != []
    """
    compound_values = {tweet.vader[2] for tweet in tweets}

    max_compound = max(compound_values)
    min_compound = min(compound_values)

    return (min_compound, max_compound)
