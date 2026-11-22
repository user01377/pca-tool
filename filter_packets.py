#!/bin/python
import time

PROTOCOL_INDEX = 4
INFO_INDEX = 6

numset = set(chr(i) for i in range(49,58))

def new_filename(filename):
    for char in filename:
        if char in numset:
            NODE_NUM = char

    return f"Node{int(NODE_NUM)}_filtered.txt"

def filter(filename):
    new_name = new_filename(filename)
    
    with open(filename) as file:
        for line in file:
            header = line
            stripped = header.strip().split()

            # when we reach the next packet, check for the next line and tokenize
            if stripped and stripped[0] == "No.":
                data_line = next(file)

                tokenized_data = data_line.strip().split()

                """
                if type is ICMP and the info contains ECHO (this is to filter out the destination unreachable packets)
                write the header line, data line, and empty line that we already parsed through earlier to check if it is a valid packet
                then run a for however long the binary is, write the write of that packet until we reach an empty string.
                """
                if tokenized_data[PROTOCOL_INDEX] == "ICMP" and tokenized_data[INFO_INDEX] == "Echo":
                    with open(new_name, "a") as new_file:
                        new_file.write(header)
                        new_file.write(data_line)
                        new_file.write(next(file))

                        next_line = next(file)
                        while next_line.strip():
                            new_file.write(next_line)

                            next_line = file.readline()

                        new_file.write("\n")

if __name__ == "__main__":
    print(f"running filter() for Node1.txt")

    filter("./Captures/Node1.txt") # HARD CODED TO RUN NODE1.TXT, WILL FIX LATER

    print("created Node1_filtered.txt")