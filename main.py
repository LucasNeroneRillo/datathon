import pandas as pd

from utils import *
from globals import *


def main():
    df = pd.read_csv(FILE_PATH)
    get_unique_values(df)


main()