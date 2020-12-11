"""
Code to format raw data from .csv file into usable Python objects.
"""
from typing import List, Dict, Optional, Tuple
import csv


class Tweet:
    """A dataclass representing the data stored about each tweet in the dataset.

    Instance Attributes:
        - sentiment: sentiment value towards climate change: -1 indicates 
        "does not support", 0 "neutral", 1 "supports", 2 "factual news"
        - content: text of the tweet
        - id: unique tweet id assigned by Twitter
        - vader: a dictionary mapping the tweet's sentiment values to their associated 
        polarity scores (neg, neu, pos, compound)

    Representation Invariants:
        - self.sentiment in {-1, 0, 1, 2}
        - len(self.content) > 0
        - self.id > 0
        - all(i in {-1, 0, 1, 2} for i in vader)
        - all(0.0 <= i <= 1.0 for i in vader.values())
    """
    sentiment: int
    content: str
    id: int
    vader: Optional[Dict[int, float]]
    
    def __init__(self, sentiment: int, content: str, id: int) -> None:
        """Initialize the a new Tweet"""
        self.sentiment = sentiment 
        self.content = content
        self.id = id
    
    def add_vader(self, vader: Dict[int, float]) -> None: 
        """Add the postive, neutral, negative and compound values calculated 
        vader_analysis as a list of 4 floats in the order described above."""
        self.vader = vader
        

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