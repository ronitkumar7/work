from dataclasses import dataclass
from typing import List
import csv


@dataclass
class Tweet:
    """A dataclass representing the data stored about each tweet in the dataset.

    Instance Attributes:
        - sentiment: sentiment value towards climate change: -1 indicates "does not support",
        0 "neutral", 1 "supports", 2 "factual news"
        - content: text of the tweet
        - id: unique tweet id assigned by Twitter

    Representation Invariants:
        - sentiment in {-1, 0, 1, 2}
        - len(content) > 0
        - id > 0
    """
    sentiment: int
    content: str
    id: int


def process(file: str) -> List[Tweet]:
    """Parse CSV file into a list of Tweets for further analysis.
    Also formats out '\n' and replaces '$q$' with single quotes.

    Our file address is twitter_sentiment_data.csv
    Preconditions:
        - file is not None
    """
    tweets_so_far = []
    with open(file, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            edited_text = row[1].replace('$q$', "'")
            edited_text = edited_text.replace('\n', '')
            tweet = Tweet(sentiment=int(row[0]), content=edited_text, id=int(row[2]))
            tweets_so_far.append(tweet)
    return tweets_so_far
