EXAMPLE = """939
7,13,x,x,59,x,31,19"""

with open("input.txt") as f:
    INPUT = f.read().strip()


def parse_raw(data_raw: str):
    timestamp, bus_list = data_raw.splitlines()
    return {
        "timestamp": int(timestamp),
        "bus_list": [int(b) for b in bus_list.split(",") if
                     b != "x"]
    }
