from utils import is_big_dataset

RESULTS_ROOT = "results/"

FILE_ROOT = "data/"
FILENAME = "complete.csv" if is_big_dataset() else "one_sensor.csv"
FILE_PATH = FILE_ROOT + FILENAME
LOCATIONS_PATH = FILE_ROOT + "routes_and_locations.csv"

DATA_COLUMNS = [
    'owner-id',  # Data type: object
    'network-id',  # Data type: object
    'date',  # Data type: int64
    'time',  # Data type: int64
    'utc-offset',  # Data type: int64
    'start-time',  # Data type: int64
    'end-time',  # Data type: int64
    'detector-id',  # Data type: object
    'status',  # Data type: object
    'lane-id',  # Data type: int64
    'lane-count',  # Data type: int64
    'lane-occupancy',  # Data type: int64
    'lane-speed',  # Data type: int64
    'small-class-count',  # Data type: int64
    'medium-class-count',  # Data type: int64
    'large-class-count',  # Data type: int64
    'device-id',  # Data type: object
    'link-direction',  # Data type: object
    'detector-type',  # Data type: object
    'sample-period',  # Data type: int64
    'device-description',  # Data type: object
    'cst-time',  # Data type: object
    'month',  # Data type: int64
    'day'  # Data type: int64
]
