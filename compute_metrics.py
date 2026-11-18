#!/bin/python


def compute(data: list[str]):
    print("called compute function in compute_metrics.py")
    # simple example: compute count, mean, min, max
    return {
        "count": len(data),
        "mean": round(sum(data) / len(data), 2),
        "min": min(data),
        "max": max(data),
    }


if __name__ == "__main__":
    print("running test code")
    test_data = range(10)
    print(f"{test_data=}")
    print(f"{compute(test_data)=}")
    # Verify method still works
    assert compute(test_data) == {"count": 10, "mean": 4.5, "min": 0, "max": 9}
