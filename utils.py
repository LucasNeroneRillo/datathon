import json
import sys

from globals import *


def get_unique_values(df):
    CHECK_UNIQUE_VALUES = [
        #'owner-id',  # Data type: object
        #'network-id',  # Data type: object
        #'date',  # Data type: int64
        #'time',  # Data type: int64
        #'utc-offset',  # Data type: int64
        #'start-time',  # Data type: int64
        #'end-time',  # Data type: int64
        'detector-id',  # Data type: object
        'status',  # Data type: object
        'lane-id',  # Data type: int64
        #'lane-count',  # Data type: int64
        #'lane-occupancy',  # Data type: int64
        #'lane-speed',  # Data type: int64
        #'small-class-count',  # Data type: int64
        #'medium-class-count',  # Data type: int64
        #'large-class-count',  # Data type: int64
        'device-id',  # Data type: object
        'link-direction',  # Data type: object
        'detector-type',  # Data type: object
        'sample-period',  # Data type: int64
        'device-description',  # Data type: object
        #'cst-time',  # Data type: object
        'month',  # Data type: int64
        #'day'  # Data type: int64
    ]

    unique_values = {
        column: df[column].unique().tolist() for column in CHECK_UNIQUE_VALUES
    }
    filename = "unique.json" if is_big_dataset() else "unique_small.json"
    with open(RESULTS_ROOT + filename, "w") as f:
        json.dump(unique_values, f, ensure_ascii=False, indent=4)


def is_big_dataset():
    return len(sys.argv) > 1 and sys.argv[1] == "big"