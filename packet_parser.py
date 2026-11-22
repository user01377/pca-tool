#!/bin/python

def create_dict(data: list):
    pass


def parse(filename: str):
    """
    the return data is a list[dict], where each dict in the list is an
    individual packet that was parsed from the NodeX_filtered.txt
    """

    parsed_packets = []

    with open(filename) as file:
        for line in file:
            header = line
            stripped = header.strip().split()

            if stripped and stripped[0] == "No.":
                data_line = next(file)

                tokenized_data = data_line.strip().split()


if __name__ == "__main__":
    """
    this main is set to parse through the Node1_filtered.txt
    running the "filter_packets.py" file will create this file.
    """
    print("parsing through Node1_filtered.txt")

    print(f"Returned data:\n{parse("./Node1_filtered.txt")}")