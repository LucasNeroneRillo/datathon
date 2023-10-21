import sys

def is_big_dataset():
    return len(sys.argv) > 1 and sys.argv[1] == "big"
