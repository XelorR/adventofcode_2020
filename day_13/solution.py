from collections import OrderedDict

EXAMPLE = """939
7,13,x,x,59,x,31,19"""

with open("input.txt") as f:
    INPUT = f.read().strip()


def parse_raw(data_raw: str):
    timestamp, bus_list = data_raw.splitlines()
    return {
        "timestamp": int(timestamp),
        "bus_list": [int(b) for b in bus_list.split(",") if b != "x"],
    }


# -= Part one =-

example_data = parse_raw(EXAMPLE)
input_data = parse_raw(INPUT)


def get_bus_next_departure(timestamp, bus_number):
    return (
        (timestamp // bus_number + 1) * bus_number
        if timestamp % bus_number != 0
        else timestamp
    )


def get_departures(data: dict) -> OrderedDict:
    bus_departures = OrderedDict()
    for b in data["bus_list"]:
        bus_departures[b] = get_bus_next_departure(data["timestamp"], b)
    return bus_departures


def part_one_answer(data: dict) -> int:
    earliest_departure = min(get_departures(data).values())
    minutes_till_earliest = earliest_departure - data["timestamp"]
    earliest_bus = [
        k for k, v in get_departures(data).items() if v == earliest_departure
    ][0]
    return earliest_bus * minutes_till_earliest


assert part_one_answer(example_data) == 295
print("Part one answer is", part_one_answer(input_data))


# -= Part two =-

def parse_raw_part_two(data_raw: str) -> list:
    if len(data_raw.splitlines()) > 1:
        return [int(b) if b != "x" else b for b in data_raw.splitlines()[1].split(",")]
    else:
        return [int(b) if b != "x" else b for b in data_raw.split(",")]


def get_departures_part_two(data_raw, timestamp: int = 3000) -> list:
    if type(data_raw) is str:
        data = parse_raw_part_two(data_raw)
    elif type(data_raw) is list:
        data = data_raw
    else:
        raise TypeError

    bus_departures = []
    for b in data:
        if type(b) is int:
            bus_departures.append([b, get_bus_next_departure(timestamp, b)])
        else:
            bus_departures.append([b, None])
    return bus_departures


def part_two_answer(data: list, ts=3000) -> int:
    bus_list = parse_raw_part_two(data)
    while True:
        bus_nearest_departures = get_departures_part_two(bus_list, ts)
        timestamps = [t[1] for t in bus_nearest_departures]
        first_timestamp = timestamps[0]
        if all([(t is None or t == first_timestamp + i) for i, t in enumerate(timestamps)]):
            return first_timestamp
        ts += 1


assert part_two_answer(EXAMPLE, 1068773) == 1068781
assert part_two_answer("17,x,13,19", 3000) == 3417
assert part_two_answer("67,7,59,61", 700000) == 754018
assert part_two_answer("67,x,7,59,61", 700000) == 779210
assert part_two_answer("67,7,x,59,61", 1000000) == 1261476
assert part_two_answer("1789,37,47,1889", 1202000000) == 1202161486

# answer is 487905974205117
# don't try to run part_two_answer on INPUT

# faster solution

import csv
import numpy as np

raw = list(csv.reader(open("input.txt")))
data = np.array([[idx, int(bus)] for idx, bus in enumerate(raw[1]) if bus != "x"])

interval = 1
time = 0
for offset, bus in data:
    while (time + offset) % bus != 0:
        time += interval
    interval = np.lcm(interval, bus)

print("Part two answer is", time)
