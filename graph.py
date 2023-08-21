import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def barGraph(yValues, nation):

    xValues = ['Wins', 'Draws', 'losses']

    plt.bar(xValues, yValues)
    plt.xlabel('Results')
    plt.title('{} all-time results'.format(nation))
    plt.show()