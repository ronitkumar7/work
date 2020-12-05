"""
Credit for vaderSentiment:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List, Tuple
from data_formatting import Tweet


def vader_values(tweet: Tweet, value: str) -> float:
    """Returns the positive, negative, neutral or compound value of a tweet as 
    calculated by the polarity_scores method of SentimentIntensityAnalyzer(). 
    
    Preconditions: 
        - value in {'neg', 'neu', 'pos', 'compound'}
    """
    analyzer = SentimentIntensityAnalyzer()
    polarity_scores_dict = analyzer.polarity_scores(tweet.content)
    return polarity_scores_dict[value]


def range_of_compound_values(tweets: List[Tweet]) -> Tuple[float, float]:
    """Returns the range of compound values of a list of given tweets in the 
    form of a tuple (min, max) where min is the lowest compound value and max 
    is the highest compound value. 
    
    Preconditions:
        - all({type(tweet) == Tweet for tweet in tweets})
        - tweets != []
    """
    compound_values = {vader_values(tweet, 'compound') for tweet in tweets}

    max_compound = max(compound_values)
    min_compound = min(compound_values)

    return (min_compound, max_compound)
