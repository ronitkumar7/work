"""All code for doing statistical analysis on tweets."""
from data_formatting import Tweet
from typing import List, Dict
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

    text = '<br>'.join(lines)  # Newlines represented by HTML '<br>' sequence

    layout = go.Layout(
        height=800,
        width=800,
        yaxis=go.layout.YAxis(domain=[0.5, 1]),
        annotations=[
            go.layout.Annotation(
                bordercolor='black',  # Remove this to hide border
                align='left',  # Align text to the left
                yanchor='top',  # Align text box's top edge
                text=text,  # Set text with '<br>' strings as newlines
                showarrow=False,  # Hide arrow head
                width=650,  # Wrap text at around 800 pixels
                xref='paper',  # Place relative to figure, not axes
                yref='paper',
                font={'family': 'Courier'},  # Use monospace font to keep nice indentation
                x=0,  # Place on left edge
                y=0.4  # Place a little more than half way down
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
    """Given tuples of positive and negative values of a list of tweets,
    plots them in a 2D plane with the x-axis as positive values and the 
    y-axis representing negative values.
    
    Preconditions:
        - all(tweet.vader is not None for tweet in tweets)
    """
    x_values = [tweet.vader['neg'] for tweet in tweets]
    y_values = [tweet.vader['pos'] for tweet in tweets]
    plt.scatter(x_values, y_values)
    plt.show()
