import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from globals import *
from utils import *

def main():
    # Open file
    filename = "cleaned_data.csv"
    df = pd.read_csv(FILE_ROOT + filename)
    df['month'] = df['month-day-hour'].apply(lambda x: x.split('-')[0])
    df['day'] = df['month-day-hour'].apply(lambda x: x.split('-')[1])
    df['hour'] = df['month-day-hour'].apply(lambda x: x.split('-')[2])

    df.plot(kind='scatter', x="lane-speed", y="lane-occupancy")

    plt.show()

main()