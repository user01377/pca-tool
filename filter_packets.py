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
    
    with open(filename) as file:
        for line in file:
            stripped = line.strip().split()

            # when we reach the next packet, check for the next line and tokenize
            if stripped and stripped[0] == "No.":
                data = next(file).strip().split()

                if data[PROTOCOL_INDEX] == "ICMP" and data[INFO_INDEX] == "Echo":
                    print(data)
                    time.sleep(0.5)
                
                


if __name__ == "__main__":
    print(f"RUNNING FOR NODE 1")

    filter("./Captures/Node1.txt")