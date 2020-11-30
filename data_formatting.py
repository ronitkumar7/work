from dataclasses import dataclass

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


def process(f: fileObject) -> List[Tweet]:
    """Parse CSV file into a list of Tweets for further analysis.
    
    Preconditions:
        - f is not None
    """
    ...