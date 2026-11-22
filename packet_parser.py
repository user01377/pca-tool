#!/bin/python


def parse(filename):
    with open(filename) as file:
        return "file opened"


if __name__ == "__main__":
    """
    this main is set to parse through the Node1_filtered.txt
    running the "filter_packets.py" file will create this file.
    """
    print("parsing through Node1_filtered.txt")

    print(f"Returned data:\n{parse("./Node1_filtered.txt")}")