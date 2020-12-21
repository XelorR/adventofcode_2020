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


def get_departures(data: dict) -> dict:
    return {b: get_bus_next_departure(data["timestamp"], b) for b in data["bus_list"]}


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

example_bus_list = example_data["bus_list"]
input_bus_list = input_data["bus_list"]
