EXAMPLE = """939
7,13,x,x,59,x,31,19"""

with open("input.txt") as f:
    INPUT = f.read().strip()


def parse_raw(data_raw: str):
    timestamp, bus_list = data_raw.splitlines()
    return {
        "timestamp": int(timestamp),
        "bus_list": [int(b) for b in bus_list.split(",") if b != "x"]
    }


example_data = parse_raw(EXAMPLE)
input_data = parse_raw(INPUT)


def get_bus_next_departure(timestamp, bus_number):
    return (timestamp // bus_number + 1) * bus_number if timestamp != 0 else timestamp


def get_departures(data: dict) -> dict:
    return {b: get_bus_next_departure(data["timestamp"], b) for
            b in
            data["bus_list"]}
