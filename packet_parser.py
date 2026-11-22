#!/bin/python

import time

def create_dict(data: list):
    """
    this is the helper function that creates the python dictionaries
    that go inside of the list that the parse() function returns

    data is structured inside of the dictionary so that the keys
    match the packet header names inside of the real NodeX_filtered.txt file
    """
    info_list = data[6:]
    info_str = " ".join(info_list)

    data_dict = {
        "No.": data[0],
        "Time": data[1],
        "Source": data[2],
        "Destination": data[3],
        "Protocol": data[4],
        "Length": data[5],
        "Info": info_str
    }

    return data_dict


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

                # append dicts created from create_dict() helper onto parsed_packets list
                parsed_packets.append(create_dict(tokenized_data))

    return parsed_packets

if __name__ == "__main__":
    """
    this main is set to parse through the Node1_filtered.txt
    running the "filter_packets.py" file will create this file.
    """
    print("parsing through Node1_filtered.txt")

    print(f"Returned data:\n{parse("./Node1_filtered.txt")}")