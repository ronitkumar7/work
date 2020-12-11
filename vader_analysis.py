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
    """Mutates each tweet to add its positive, negative, neutral, and compound values as 
    calculated by the polarity_scores method of SentimentIntensityAnalyzer().
    """
    analyzer = SentimentIntensityAnalyzer()
    for tweet in tweets:
        tweet.vader = analyzer.polarity_scores(tweet.content)
