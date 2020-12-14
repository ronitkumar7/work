"""CSC110 Project: Climate Change Sentiment on Twitter: Data Formatting

Module Description:
====================
The module contains Tweet dataclass and the function that processes the raw CSV file
into a list of Tweets. It also contains a function that sorts the list of tweets by opinion value.
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
        - sentiment: a dictionary mapping of sentiment analysis scores (neg, neu, pos, compound)
        to their respective values

    Representation Invariants:
        - self.opinion in {-1, 0, 1, 2}
        - len(self.content) > 0
        - self.sentiment.keys() == ['neg', 'neu', 'pos', 'compound']
        - 0.0 <= self.sentiment['neg'] <= 1.0
        - 0.0 <= self.sentiment['neu'] <= 1.0
        - 0.0 <= self.sentiment['pos'] <= 1.0
        - -1.0 <= self.sentiment['compound'] <= 1.0

    Sample Usage:
    >>> example_tweet = Tweet(opinion=0, content='David is cool!')
    >>> example_tweet.sentiment is None
    True
    """
    opinion: int
    content: str
    sentiment: Optional[Dict[str, float]] = None


def process(file: str) -> List[Tweet]:
    """Access filepath provided and parse each row in the file into an instance of Tweet.

    Return a list of all such instances of Tweet.

    Apply the following additional formatting to the second column (which should be a string):
        - Remove newline characters ('\n')
        - Replace `$q$` with an apostrophe
        - Re-encode malformed text as UTF-8

    Preconditions:
        - file != ''
        - file is in CSV format
    """
    tweets_so_far = []
    with open(file, encoding="utf8") as csv_file:
        # Creates a csv reader to read the csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skips the header row
        for row in csv_reader:
            try:
                last_row = ''
                while last_row != row[1]:
                    last_row = row[1]
                    row[1] = row[1].encode('cp1252').decode('utf-8')
            except ValueError:
                pass
            finally:
                # Replaces some formatting characters with the characters they represent.
                edited_text = row[1].replace('$q$', "'").replace('&amp;', '&')
                # Creates an instance of the Tweet class with the edited text
                tweet = Tweet(opinion=int(row[0]), content=edited_text)
                tweets_so_far.append(tweet)  # Appends the tweet to the list
    for tweet in tweets_so_far:
        filter_tweet(tweet)  # Helper function called to filter tweets
    return tweets_so_far


def sort_tweets(tweets: List[Tweet]) -> Dict[int, List[Tweet]]:
    """Returns a dictionary of 4 keys, mapping an opinion value to the subset (list) of 'tweets'
    which have that opinion value.

    Preconditions:
        - tweets != []
        - all(t.sentiment is not None for t in tweets)
    """
    # Initializing the dictionary where opinion values map to a list of tweets
    # that have the same opinion value as the key
    tweet_dict = {-1: [], 0: [], 1: [], 2: []}
    for tweet in tweets:  # Loops through every tweet
        for key in tweet_dict:  # Loops through every possible opinion value
            if tweet.opinion == key:
                # If the tweet has the same opinion value as the key,
                # the tweet is appended to the list the key maps to in the dictionary
                tweet_dict[key].append(tweet)
    return tweet_dict


def filter_tweet(tweet: Tweet) -> None:
    """Removes some common parts of a tweet that do not reflect any sentiment and hence
    will falsely give a neutral value according to vaderSentiment. This will produce
    a more accurate polarity score.
    """
    remove_keyword = {'http', '@', '#', 'RT'}
    # most common beginnings of words that will be identified falsely as neutral.
    split_tweet = tweet.content.split()
    remove_strings = []
    for string in split_tweet:
        for keyword in remove_keyword:
            if string.startswith(keyword):
                remove_strings.append(string)
    for string in remove_strings:
        split_tweet.remove(string)
    final_tweet = ' '.join(split_tweet)
    tweet.content = final_tweet


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
