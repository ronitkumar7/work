"""All code for doing statistical analysis on tweets."""
from data_formatting import Tweet, sort_tweets
from typing import List, Dict, Tuple
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import statistics


def min_max_values(data: List[float]) -> Tuple[float, float]:
    """Returns the minimum and maximum of a list of numbers in a tuple (min, max).
    
    Preconditions:
        - data != []
    """
    return (min(data), max(data))


def frequency(tweets: List[Tweet]) -> Dict[str, int]:
    """Return the frequency of positive, negative and neutral tweets in the
    list of tweets provided.
    
    Precondition:
        - all(t.vader is not None for t in tweets)
    """
    news_neutral_tweets = [tweet for tweet in tweets if tweet.sentiment in {0, 2}]
    range_compound = min_max_values([t.vader['compound'] for t in news_neutral_tweets])
    freq_neg = 0
    freq_pos = 0
    freq_neu = 0
    
    for tweet in tweets:
        if tweet.vader['compound'] < range_compound[0]:
            freq_neg += 1
        elif tweet.vader['compound'] > range_compound[1]:
            freq_pos += 1
        elif range_compound[0] <= tweet.vader['compound'] <= range_compound[1]:
            freq_neu += 1
    
    return {'positive': freq_pos, 'neutral': freq_neu, 'negative': freq_neg}


def normal_histogram(tweets: List[Tweet]) -> None:
    """Displays a normal histogram in plotly containing the compound values of each tweet
     in tweets.

    Precondition:
        - all(t.vader is not None for t in tweets)
    """
    compound_values = [tweet.vader['compound'] for tweet in tweets]
    summary_data = summary(compound_values)
    lines = [
        'Mean :' + str(summary_data['mean']),
        'Median :' + str(summary_data['median']),
        'Standard Deviation :' + str(summary_data['stdev']),
        'Range :' + str(summary_data['range'])
    ]

    text = '<br>'.join(lines)  # HTML '<br>' sequence gives newlines

    layout = go.Layout(
        height=800,
        width=800,
        yaxis=go.layout.YAxis(domain=[0.5, 1]),
        annotations=[
            go.layout.Annotation(
                bordercolor='black',
                align='left',
                yanchor='top',  # Align text box's top edge with y axis
                text=text,
                showarrow=False,
                width=650,
                xref='paper',  # Place relative to figure, not axes
                yref='paper',
                font={'family': 'Courier'},
                x=0,  # Coordinates start from top left corner
                y=0.4
            )
        ])
    fig = go.Figure(data=[go.Histogram(x=compound_values, histnorm='probability')], layout=layout)
    fig.update_traces(xbins_size=0.01, selector=dict(type='histogram'))
    fig.show()


def summary(data: List[float]) -> Dict[str, float]:
    """Return a dictionary of summary statistics for a list of numbers.

    Mappings:
        - 'mean': mean of the data
        - 'median': median of the data
        - 'stdev': sample standard deviation of the data
        - 'range': (statistical) range of the data
    
    Preconditions:
        - len(data) > 0
    """
    return {
        'mean': statistics.mean(data),
        'median': statistics.median(data),
        'stdev': statistics.stdev(data),
        'range': max(data) - min(data)
    }


def plot_pos_neg(tweets: List[Tweet]) -> None:
    """Plots each tweet as a point where the x-coordinate is the negative value
    and the y-coordinate is the positive value. 
    
    Preconditions:
        - all(tweet.vader is not None for tweet in tweets)
    """
    x_values = [tweet.vader['neg'] for tweet in tweets]
    y_values = [tweet.vader['pos'] for tweet in tweets]
    plt.scatter(x_values, y_values, s=2, marker="o")
    plt.show()
    
def plot_compound(tweets: List[Tweet]) -> None:
    """Plots each tweet as a point where the x-coordinate is the compound value
    and the y-coordinate is fixed for each tweet type 
    (-1 for 'does not support', 0 for 'neutral', 1 for 'supports' and 2 for 'news')
    """
    sorted_tweets = sort_tweets(tweets)
    not_support = [tweet.vader['compound'] for tweet in sorted_tweets[-1]]
    neutral = [tweet.vader['compound'] for tweet in sorted_tweets[0]]
    support = [tweet.vader['compound'] for tweet in sorted_tweets[1]]
    news = [tweet.vader['compound'] for tweet in sorted_tweets[2]]
    y_not_support = [-1 for _ in range(0, len(not_support))]
    y_neutral = [0 for _ in range(0, len(neutral))]
    y_support = [1 for _ in range(0, len(support))]
    y_news = [2 for _ in range(0, len(news))]
    plt.scatter(not_support, y_not_support, s=0.1, marker='.')
    plt.scatter(neutral, y_neutral, s=0.1, marker='.')
    plt.scatter(support, y_support, s=0.1, marker='.')
    plt.scatter(news, y_news, s=0.1, marker='.')
    plt.show()
    # still need to make plot wider to make difference more visible
