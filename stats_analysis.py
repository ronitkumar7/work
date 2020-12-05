"""All code for doing statiscal analysis on tweets."""
from data_formatting import Tweet
from typing import List, Dict
from vader_analysis import range_of_compound_values, vader_values


def frequency(tweets: List[Tweet]) -> Dict[str, int]:
    """Return the frequency of positive, negative and neutral tweets in the
    list of tweets provided."""
    range_compound = range_of_compound_values(tweets)
    tweets_values = [(tweet, vader_values(tweet, 'compound')) for tweet in tweets]
    freq_neg = 0
    freq_pos = 0
    freq_neu = 0
    for tweet in tweets_values:
        if tweet[1] < range_compound[0]:
            freq_neg += 1
        elif tweet[1] > range_compound[1]:
            freq_pos += 1
        elif range_compound[0] <= tweet[1] <= range_compound[1]:
            freq_neu += 1
    return {'positive': freq_pos, 'neutral': freq_neu, 'negative': freq_neg}
