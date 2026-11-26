#!/bin/python


def compute(data: list[str], node_sum: int=1):
    print("called compute function in compute_metrics.py")
    # simple example: compute count, mean, min, max

    requests_sent = 0
    requests_received = 0
    replies_sent = 0
    replies_received = 0

    req_sent = 0
    req_received = 0
    req_sent = 0
    req_received = 0
    
    rtt_list = []
    reply_delay = []
    hop_counts = []

    requests_map = {}

    node_ips = {1: "192.168.100.1", 2: "192.168.100.2", 3: "192.168.100.1", 4: "192.168.100.2"}
    node_ip = node_ips.get(node_num, "192.168.100.1")

    for pkt in data:
        src = pkt.get("source")

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
