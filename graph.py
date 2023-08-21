import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def barGraph(yValues, xValues, nation, colors):
    #Create Bar Graph
    bars = plt.bar(xValues, yValues)
    plt.xlabel('Results')
    plt.title('{} all-time results'.format(nation))

    #Set bar colors
    for bar, color in zip(bars, colors):
        bar.set_color(color)

    plt.show()