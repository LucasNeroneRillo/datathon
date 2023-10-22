import matplotlib
import pandas as pd

from globals import *
from utils import *

def main():
    # Open file
    filename = "cleaned_data.csv"
    df = pd.read_csv(FILE_ROOT + filename)

    
    