#!/bin/python


def filter(data: list):
    print("called filter function in filter_packets.py")
    # simple example: filter vowels and end of alphabet
    return [c for c in data if c not in "AEIOU" + "VWXYZ"]


if __name__ == "__main__":
    print("running test code")
    test_data = list("ABCDEFGTUVWXYZ")
    print(f"{test_data=}")
    print(f"{filter(test_data)=}")
    # Verify method still works
    assert filter(test_data) == list("BCDFGT")
