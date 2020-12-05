"""
Driver file for the Climate Change Sentiment on Twitter project.
"""

import data_formatting
import vader_analysis
import stats_analysis

if __name__ == "__main__":

    # Data formatting
    f = open('dataset.csv', 'r')

    dataset = data_formatting.process(f)

    # VADER sentiment analysis
    vader_analysis.analyze(dataset)

    # Statistical analysis
    #
    # Call any functions related to statistical analysis
    ...

    # Interactive pygame
    #
    # Create window and run interactive module
    ...