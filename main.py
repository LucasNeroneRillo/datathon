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
    df['month-day-hour'] = df.apply(lambda row: f"{row['month']:02}-{row['day']:02}-{(row['time'] // 10000):02}", axis=1)
    df['detector-id'] = df['detector-id'].apply(lambda x: int(re.search(r'\d+', x).group())).astype(str)# + df['link-direction']

    # Group by hour/detector
    df = df.groupby(['month-day-hour', 'detector-id']).agg({
        'lane-count': 'sum',
        'lane-occupancy': lambda x: np.average(x, weights=df.loc[x.index, 'sample-period']),
        'lane-speed': lambda x: np.average(x, weights=df.loc[x.index, 'lane-count']),
    }).reset_index()

    # Generate extra columns
    df['month'] = df['month-day-hour'].apply(lambda x: x.split('-')[0])
    df['day'] = df['month-day-hour'].apply(lambda x: x.split('-')[1])
    df['hour'] = df['month-day-hour'].apply(lambda x: x.split('-')[2])
    df['month-day'] = df['month-day-hour'].apply(lambda x: x.split('-')[0] + '-' + x.split('-')[1])
    datetimes = pd.to_datetime(df['month-day-hour'], format='%m-%d-%H').apply(lambda x: x.replace(year=2022))
    df['day-of-week'] = datetimes.dt.strftime('%a')

    # Save results
    filename = "cleaned_data.csv" if is_big_dataset() else "cleaned_data_small.csv"
    df.to_csv(FILE_ROOT + filename)

main()