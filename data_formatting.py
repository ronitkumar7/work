"""
Code to format raw data from .csv file into usable Python objects.
"""
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import csv

@dataclass
class Tweet:
    """A dataclass representing the data stored about each tweet in the dataset.

    Instance Attributes:
        - sentiment: sentiment value towards climate change: -1 indicates 
        "does not support", 0 "neutral", 1 "supports", 2 "factual news"
        - content: text of the tweet
        - id: unique tweet id assigned by Twitter
        - vader: a dictionary mapping of polarity score types [neg, neu, pos, compound] to
        their respective values

    Representation Invariants:
        - self.sentiment in {-1, 0, 1, 2}
        - len(self.content) > 0
        - self.id > 0
        - self.vader.keys() == ['neg', 'neu', 'pos', 'compound']
        - all(0.0 <= i <= 1.0 for i in self.vader.values())
    """
    sentiment: int
    content: str
    id: int
    vader: Optional[Dict[str, float]] = None


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
            edited_text = row[1].replace('$q$', "'").replace('\n', '')
            tweet = Tweet(sentiment=int(row[0]), content=edited_text, id=int(row[2]))
            tweets_so_far.append(tweet)
    return tweets_so_far


def sort_tweets(tweets: List[Tweet]) -> Dict[int, List[Tweet]]:
    """Returns a dictionary of 4 keys, each key corresponding to a sentiment 
    value.
    
    Preconditions:
        - tweets != []
    """
    tweet_dict = {-1: [], 0: [], 1: [], 2: []}
    for tweet in tweets:
        for key in tweet_dict:
            if tweet.sentiment == key:
                tweet_dict[key].append(tweet)
    return tweet_dict
