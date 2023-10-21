import json
import pandas as pd

from utils import *
from globals import *


def main():
    filename = "complete.csv" if is_big_dataset() else "one_sensor.csv"
    df = pd.read_csv(FILE_ROOT + filename)
    get_unique_values(df)


main()