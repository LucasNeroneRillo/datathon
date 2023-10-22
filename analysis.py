import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


from globals import *
from utils import *

df = pd.read_csv(FILE_ROOT + "cleaned_data.csv")

def main():
    # TODO: ignore before 8am
    ############################################################

    dfs = {
        'hour': aggregate_by(['hour']),
        'day-of-week': aggregate_by(['day-of-week']),
        'month-day': aggregate_by(['month-day'])
    }
    
    #dfs['day-of-week'].plot(kind="bar", x="day-of-week", y="lane-speed")
    
    # Set the new x-axis ticks with only desired num of ticks
    #desired_num_ticks = 10
    #current_ticks = plt.xticks()[0]
    #step = len(current_ticks) // (desired_num_ticks - 1)
    #new_ticks = current_ticks[::step]
    #plt.xticks(new_ticks)
    heatmap()
    


def aggregate_by(column_list):
    return df.groupby(column_list).agg({
        'lane-count': 'sum',
        'lane-occupancy': 'mean',
        'lane-speed': lambda x: np.average(x, weights=df.loc[x.index, 'lane-count']),
    }).reset_index()


def heatmap():
    # One row for each combination of detector id and day
    df2 = df.copy()
    df2 = aggregate_by(['detector-id', 'month-day'])
    
    # Filter detectors that do not have data for every day
    counts = df2['detector-id'].value_counts()
    max_frequency = counts.max()
    max_frequency_ids = counts[counts == max_frequency].index.tolist()
    df2 = df2[df2['detector-id'].isin(max_frequency_ids)]
    pivot_df = df2.pivot(index='detector-id', columns='month-day', values='lane-speed')
    
    # Create heatmap
    plt.figure(figsize=(30, 8))
    sns.heatmap(pivot_df, cmap='RdYlGn', annot=False, fmt=".1f", linewidths=0.5)
    plt.title('Lane Speed Heatmap')
    plt.xlabel('Date')
    plt.ylabel('Detector ID')
    plt.show()

main()