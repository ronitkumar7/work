"""
Credit for vaderSentiment:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List, Dict
from data_formatting import Tweet

def analyse(data: List[Tweet]) -> Dict[Tweet.content, Dict[str, int]]:
    """ Return a mapping of each tweet to its sentiment data.


    """
    analyzer = SentimentIntensityAnalyzer()
    for tweet in data:
        vs = analyzer.polarity_scores(tweet.content)

    return ...
