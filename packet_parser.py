#!/bin/python


def parse(data: list):
    print("called parse function in packet_parser.py")
    # simple example: convert letter to value in alphabet
    return [ord(c) - ord("A") + 1 for c in data]


if __name__ == "__main__":
    print("running test code")
    test_data = list("ABCDEF")
    print(f"{test_data=}")
    print(f"{parse(test_data)=}")
    # Verify method still works
    assert parse(test_data) == [1, 2, 3, 4, 5, 6]
