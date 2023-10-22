import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


from globals import *
from utils import *


df = pd.read_csv(FILE_ROOT + "cleaned_data.csv")


def main():
    x1, x2, x3 = "hour", "day-of-week", "month-day"
    chosen_x = x1
    
    y1, y2 = "lane-speed", "lane-occupancy"
    chosen_y = y1

    #bar_graph(chosen_x, chosen_y)
    heatmap(chosen_x, chosen_y)


def aggregate_by(column_list):
    return df.groupby(column_list).agg({
        'lane-count': 'sum',
        'lane-occupancy': 'mean',
        'lane-speed': lambda x: np.average(x, weights=df.loc[x.index, 'lane-count']),
    }).reset_index()


def bar_graph(chosen_x, chosen_y):
    aggregate_by([chosen_x]).plot(kind="bar", x=chosen_x, y=chosen_y)

    # Set the new x-axis ticks with only desired num of ticks
    if chosen_x == "month-day":
        desired_num_ticks = 10
        current_ticks = plt.xticks()[0]
        step = len(current_ticks) // (desired_num_ticks - 1)
        new_ticks = current_ticks[::step]
        plt.xticks(new_ticks)
    plt.show()


def heatmap(chosen_x, chosen_y):
    # One row for each combination of detector id and day
    df2 = df.copy()
    df2 = aggregate_by(['detector-id', chosen_x])
    
    # Filter detectors that do not have data for every day
    counts = df2['detector-id'].value_counts()
    max_frequency = counts.max()
    max_frequency_ids = counts[counts == max_frequency].index.tolist()
    df2 = df2[df2['detector-id'].isin(max_frequency_ids)]
    pivot_df = df2.pivot(index='detector-id', columns=chosen_x, values=chosen_y)
    
    # Create heatmap
    plt.figure(figsize=(30, 8))
    sns.heatmap(pivot_df, cmap='RdYlGn', annot=False, fmt=".1f", linewidths=0.5)
    plt.title(f'{chosen_y} heatmap')
    plt.ylabel('Detector ID')
    plt.show()


main()