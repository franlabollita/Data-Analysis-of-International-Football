import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def barGraph(yValues, xValues, title, colors=None):
    #Create Bar Graph
    bars = plt.bar(xValues, yValues)
    plt.xlabel('Results')
    plt.title(title)

    #Set bar colors
    if colors != None:
        for bar, color in zip(bars, colors):
            bar.set_color(color)

    plt.show()

def pieChart(values, labels, title, colors=None):
    if colors is None:
        # Use default colors if colors parameter is not provided
        colors = plt.cm.Paired.colors
    #graph pie chart
    pieChart = plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
    plt.title(title)

    plt.show()
