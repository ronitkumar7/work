"""
CSC110 Project: Climate Change Sentiment on Twitter: Vader Analysis

Module Description:
====================
The module contains the function that utilizes the vaderSentiment Library to analyse
the text of the Tweet and assigns the resulting values to the sentiment attribute
in the Tweet dataclass.
=====================
Credit for vaderSentiment:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""
from typing import List
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from data_formatting import Tweet


def add_vader_to_tweets(tweets: List[Tweet]) -> None:
    """Mutates each tweet to add its positive, negative, neutral, and compound values as
    calculated by the polarity_scores method of SentimentIntensityAnalyzer().
    """
    analyzer = SentimentIntensityAnalyzer()
    for tweet in tweets:
        tweet.sentiment = analyzer.polarity_scores(tweet.content)


if __name__ == "__main__":
    import python_ta
    import python_ta.contracts
    import doctest

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'vaderSentiment.vaderSentiment',
                          'data_formatting'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    doctest.testmod(verbose=True)
