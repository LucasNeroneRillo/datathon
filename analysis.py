import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from globals import *
from utils import *

def main():
    # Open file
    filename = "cleaned_data.csv"
    df = pd.read_csv(FILE_ROOT + filename)

    df.plot(kind='scatter', x="lane-speed", y="lane-occupancy")

    plt.show()

main()