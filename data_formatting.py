"""
Code to format raw data from .csv file into usable Python objects.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import csv


@dataclass
class Tweet:
    """A dataclass representing the data stored about each tweet in the dataset.

    Instance Attributes:
        - opinion: value dictates opinon towards climate change: -1 indicates
        "does not support", 0 "neutral", 1 "supports", 2 "factual news"
        - content: text of the tweet
        - sentiment: a dictionary mapping of polarity score types [neg, neu, pos, compound] to
        their respective values

    Representation Invariants:
        - self.opinion in {-1, 0, 1, 2}
        - len(self.content) > 0
        - self.id > 0
        - self.sentiment.keys() == ['neg', 'neu', 'pos', 'compound']
        - all(0.0 <= i <= 1.0 for i in self.sentiment.values())

    Sample Usage:
    >>> some_tweet = Tweet(opinion=0, content='David is cool!')
    >>> some_tweet.sentiment is None
    True
    """
    opinion: int
    content: str
    sentiment: Optional[Dict[str, float]] = None


def process(file: str) -> List[Tweet]:
    """Parse CSV file into a list of Tweets for further analysis.
    Also, remove newline characters ('\n') and replace `$q$` with an apostrophe.

    Preconditions:
        - file != ''
    """
    tweets_so_far = []
    with open(file, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            try:
                last_row = ''
                while last_row != row[1]:
                    last_row = row[1]
                    row[1] = row[1].encode('cp1252').decode('utf-8')
            except:
                pass
            finally:
                edited_text = row[1].replace('$q$', "'").replace('&amp;', '&')
                tweet = Tweet(opinion=int(row[0]), content=edited_text)
                tweets_so_far.append(tweet)
    return tweets_so_far


def sort_tweets(tweets: List[Tweet]) -> Dict[int, List[Tweet]]:
    """Returns a dictionary of 4 keys, each key corresponding to a sentiment value.

    Preconditions:
        - tweets != []
    """
    tweet_dict = {-1: [], 0: [], 1: [], 2: []}
    for tweet in tweets:
        for key in tweet_dict:
            if tweet.opinion == key:
                tweet_dict[key].append(tweet)
    return tweet_dict


if __name__ == "__main__":
    import python_ta
    import python_ta.contracts
    import doctest

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'dataclasses', 'csv'],
        'allowed-io': ['process'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    doctest.testmod(verbose=True)
