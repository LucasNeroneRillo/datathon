import json
import re
import pandas as pd

from utils import *
from globals import *


def main():
    filename = "Wavetronix Nov Dev 2023.csv" if is_big_dataset() else "one_sensor.csv"
    df = pd.read_csv(FILE_ROOT + filename)
    columns_to_remove = ['owner-id', 'network-id', 'date', 'utc-offset', 'start-ime', 'end-time', 'small-class-count', 'medium-class-count', 'large-class-count', 'device-id', 'detector-type', 'cst-time']

    df = df.drop(columns=columns_to_remove)
    

    df = df[df['status'] == 'OK']
    df = df[df['device-description'] == 'NORMAL']
    df = df[df['time'] >= 80000]
    df = df[df['time'] <= 235900]
    # indexAge = df[ (df['status'] == 'OK') | (df['device-description'] == 'NORMAL') ].index
    # df.drop(indexAge , inplace=True)

    # print(df['detector-id'])
    # print(df['detector-id'].dtype)
    print(df.info())
    print(df.shape[0])


# Function to update detector-id to only return 19
def update_detector_id(row):
    for text_value in row['detector-id']:
        return int(re.search(r'\d+', row['detector-id']).group())


# Function to make where the OK is not found in Status and make it an empty row
def update_status(row):
    target = 'OK'
    for text_value in row['status']:
        if target in row['status']:
            return row['status']
        else:
            
            return None
        
# Function to ensure device-description is NORMAL
def update_device_description(row):
    target = 'NORMAL'
    #/for text_value in row['device-description']:
    if target in row['device-description']:
        return row['device-description']
    else:
        return None


main()