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

# assert part_two_answer(example_bus_list, 1068773) == 1068781
# assert part_two_answer([int(b) for b in "17,x,13,19".split(",") if b != "x"], 3000) == 3417
# assert part_two_answer([int(b) for b in "67,7,59,61".split(",") if b != "x"], 700000) == 754018
# assert part_two_answer([int(b) for b in "67,x,7,59,61".split(",") if b != "x"], 700000) == 779210
# assert part_two_answer([int(b) for b in "67,7,x,59,61".split(",") if b != "x"], 1000000) == 1261476
# assert part_two_answer([int(b) for b in "1789,37,47,1889".split(",") if b != "x"], 12000000) == 1202161486
