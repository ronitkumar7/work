"""CSC110 Project: Climate Change Sentiment on Twitter: Stats analysis

Module Description:
====================
The module contains the functions that perform statistical operations on the data
and then graph it using plotly.
"""

from typing import List, Dict, Tuple
import statistics
import plotly.graph_objects as go
from data_formatting import Tweet


def compare_frequency_vader(sorted_tweets: Dict[int, List[Tweet]]) -> None:
    """Displays a grouped bar chart with the x_values being the four different
    types of opinions. For each opinion, there are three bars, each representing
    the frequency of positive, neutral and negative tweets. """
    freq_dict = frequency(sorted_tweets)
    # Helper function to calculate percentage of frequency
    y_pos = [freq_dict[x]['pos'] for x in [-1, 0, 1, 2]]
    y_neu = [freq_dict[x]['neu'] for x in [-1, 0, 1, 2]]
    y_neg = [freq_dict[x]['neg'] for x in [-1, 0, 1, 2]]
    opinion = ['does not support', 'neutral', 'support', 'news']  # x-axis labels
    fig = go.Figure(data=[
        go.Bar(name='Positive', x=opinion, y=y_pos),
        go.Bar(name='Neutral', x=opinion, y=y_neu),
        go.Bar(name='Negative', x=opinion, y=y_neg)
    ])

    fig.update_layout(barmode='group',
                      title='Percentage of tweets of different sentiments within each opinion',
                      yaxis_title='Percentage of tweets',
                      xaxis_title='Opinion')
    fig.show()


def normal_histogram(tweets: List[Tweet]) -> None:
    """Displays a normal histogram in plotly containing the compound values of each tweet
     in tweets.

    Precondition:
        - all(t.sentiment is not None for t in tweets)
    """
    # Retrieves the compound scores of each tweet
    compound_values = [tweet.sentiment['compound'] for tweet in tweets]
    # Compute the summary statistics of the compound values
    summary_data = summary(compound_values)
    # Store the summary statistics of the compound values in text form to add as annotation
    lines = [
        'Mean :' + str(summary_data['mean']),
        'Median :' + str(summary_data['median']),
        'Standard Deviation :' + str(summary_data['stdev']),
        'Range :' + str(summary_data['range'])
    ]

    text = '<br>'.join(lines)  # HTML '<br>' sequence gives newlines
    # Adds the annotation that displays the summary statistics in a box below the graph.
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
    # Creates the figure object that draws the histogram and takes in the annotation created above
    fig = go.Figure(data=[go.Histogram(x=compound_values, histnorm='probability')], layout=layout)
    fig.update_traces(xbins_size=0.01, selector=dict(type='histogram'))
    fig.update_layout(title='Percentage of frequency of tweets against compound value range',
                      xaxis_title='Compound value range',
                      yaxis_title='Percentage of occurrence')
    # Shows the figure object
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

    Precondition:
        - all(t.sentiment is not None for t in tweets)
    """
    # Retrieves the negative and positive scores for each tweet
    x_values = [tweet.sentiment['neg'] for tweet in tweets]
    y_values = [tweet.sentiment['pos'] for tweet in tweets]
    # Creates a figure object that displays a scatter plot with the negative
    # scores on the x-axis, and positive scores on the y-axis
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='markers'))
    fig.update_layout(title='Scatter plot of positive against negative polarity score',
                      xaxis_title='Negative polarity score',
                      yaxis_title='Positive polarity score')
    fig.show()


def plot_compound(sorted_tweets: Dict[int, List[Tweet]]) -> None:
    """Displays a box plot for each opinion.
    """
    # Retrieves compound values for each list of tweets, which have been sorted by opinion value.
    not_support = [tweet.sentiment['compound'] for tweet in sorted_tweets[-1]]
    neutral = [tweet.sentiment['compound'] for tweet in sorted_tweets[0]]
    support = [tweet.sentiment['compound'] for tweet in sorted_tweets[1]]
    news = [tweet.sentiment['compound'] for tweet in sorted_tweets[2]]
    # Creates an empty figure object
    fig = go.Figure()
    # Adds each box plot to the figure object
    fig.add_trace(go.Box(x=not_support, name='Against Climate Change'))
    fig.add_trace(go.Box(x=neutral, name='Neutral'))
    fig.add_trace(go.Box(x=support, name='In Support Of Climate Change'))
    fig.add_trace(go.Box(x=news, name='News'))
    fig.update_layout(title='Box plot for each opinion',
                      xaxis_title='Compound value',
                      yaxis_title='Opinion')
    fig.show()


#############################################################################
# Helper functions:
#############################################################################

def min_max_values(data: List[float]) -> Tuple[float, float]:
    """Returns the minimum and maximum of a list of numbers in a tuple (min, max).

    Preconditions:
        - data != []
    """
    return (min(data), max(data))


def frequency(sorted_tweets: Dict[int, List[Tweet]]) -> Dict[int, Dict[str, int]]:
    """Return the percentage of positive, negative and neutral tweets in the
    dictionary of sorted tweets provided. The frequency of the three types of
    values are calculated for each opinion in the dictionary provided. The function
    returns a dictionary that maps each opinion to a dictionary that maps each type
    of tweet (pos, neu, neg) to the percentage of its frequency .

    Precondition:
        - list(sorted_tweets.keys()) == [-1, 0, 1, 2]
    """
    freq_dict = {-1: {}, 0: {}, 1: {}, 2: {}}
    for key in sorted_tweets:
        freq_neg = 0
        freq_pos = 0
        freq_neu = 0
        for tweet in sorted_tweets[key]:
            if tweet.sentiment['compound'] <= -0.05:
                # a negative string according to vaderSentiment
                freq_neg += 1
            elif tweet.sentiment['compound'] >= 0.05:
                # a positive string according to vaderSentiment
                freq_pos += 1
            else:
                # a neutral string according to vaderSentiment
                freq_neu += 1
        percentage_neg = freq_neg / len(sorted_tweets[key])
        percentage_neu = freq_neu / len(sorted_tweets[key])
        percentage_pos = freq_pos / len(sorted_tweets[key])
        freq_dict[key] = {'pos': percentage_pos, 'neu': percentage_neu, 'neg': percentage_neg}
    return freq_dict


if __name__ == "__main__":
    import python_ta
    import python_ta.contracts
    import doctest

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'data_formatting', 'plotly.graph_objects',
                          'statistics'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    doctest.testmod(verbose=True)
