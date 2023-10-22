import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


from globals import *
from utils import *


df = pd.read_csv(FILE_ROOT + "cleaned_data.csv")


def main():
    o1, o2, o3 = "hour", "day-of-week", "month-day"
    chosen = o2

    #occupancy_bar_graph(chosen)
    traffic_heatmap(chosen)


def aggregate_by(column_list):
    return df.groupby(column_list).agg({
        'lane-count': 'sum',
        'lane-occupancy': 'mean',
        'lane-speed': lambda x: np.average(x, weights=df.loc[x.index, 'lane-count']),
    }).reset_index()


def occupancy_bar_graph(time_type):
    aggregate_by([time_type]).plot(kind="bar", x=time_type, y="lane-occupancy")

    # Set the new x-axis ticks with only desired num of ticks
    if time_type == "month-day":
        desired_num_ticks = 10
        current_ticks = plt.xticks()[0]
        step = len(current_ticks) // (desired_num_ticks - 1)
        new_ticks = current_ticks[::step]
        plt.xticks(new_ticks)
    plt.show()


def traffic_heatmap(time_type):
    # One row for each combination of detector id and day
    df2 = df.copy()
    df2 = aggregate_by(['detector-id', time_type])
    
    # Filter detectors that do not have data for every day
    counts = df2['detector-id'].value_counts()
    max_frequency = counts.max()
    max_frequency_ids = counts[counts == max_frequency].index.tolist()
    df2 = df2[df2['detector-id'].isin(max_frequency_ids)]
    pivot_df = df2.pivot(index='detector-id', columns=time_type, values='lane-speed')
    
    # Create heatmap
    plt.figure(figsize=(30, 8))
    sns.heatmap(pivot_df, cmap='RdYlGn', annot=False, fmt=".1f", linewidths=0.5)
    plt.title('Lane Speed Heatmap')
    plt.ylabel('Detector ID')
    plt.show()


main()