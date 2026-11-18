#!/bin/python

from filter_packets import *
from packet_parser import *
from compute_metrics import *

# imports here only for random data, remove in your code
import random
import string

def main():
    all_data = [random.choices(string.ascii_uppercase, k=15) for _ in range(4)]

    for data in all_data:
        print(f"Processing {data}")
        data_filtered = filter(data)
        # print(f"{data_filtered=}")
        data_parsed = parse(data_filtered)
        # print(f"{data_parsed=}")
        data_computed = compute(data_parsed)
        # print(f"{data_computed=}")
        print(f"Results of processing {sorted(data)}:")
        print(f"{data_computed}")
        print()

if __name__ == "__main__":
    main()
