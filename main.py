import json
import numpy as np
import re
import pandas as pd

from utils import *
from globals import *


def main():
    # Open file
    filename = "Wavetronix Nov Dev 2023.csv" if is_big_dataset() else "one_sensor.csv"
    df = pd.read_csv(FILE_ROOT + filename)
    
    # Drop unnecessary columns
    columns_to_remove = ['owner-id', 'network-id', 'date', 'utc-offset', 'start-ime', 'end-time', 'small-class-count', 'medium-class-count', 'large-class-count', 'device-id', 'detector-type', 'cst-time']
    df = df.drop(columns=columns_to_remove)
    
    # Clean data
    df = df[df['lane-count'] != 0]
    df = df[df['status'] == 'OK']
    df = df[df['device-description'] == 'NORMAL']
    df = df[df['time'] >= 80000]
    df = df[df['time'] <= 235900]
    df['month-day-hour'] = df['month'].astype(str) + '-' + df['day'].astype(str) + '-' + df['time'].astype(str).str[:2]
    df['detector-id'] = df['detector-id'].apply(lambda x: int(re.search(r'\d+', x).group())).astype(str) + df['link-direction']

    # Group by hour/detector
    df = df.groupby(['month-day-hour', 'detector-id']).agg({
        'lane-count': 'sum',
        'lane-occupancy': lambda x: np.average(x, weights=df.loc[x.index, 'sample-period']),
        'lane-speed': lambda x: np.average(x, weights=df.loc[x.index, 'lane-count']),
    }).reset_index()

    filename = "cleaned_data.csv" if is_big_dataset() else "cleaned_data_small.csv"
    df.to_csv(FILE_ROOT + filename)

    #print(df)
    #print(df.info())
    #print(df.shape[0])



main()