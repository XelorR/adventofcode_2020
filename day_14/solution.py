import re

EXAMPLE = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

with open("input.txt") as f:
    INPUT = f.read().strip()


def parse_raw(data_raw: str):
    data = [c.split(" = ") for c in data_raw.splitlines()]
    return [
        c if c[0] == "mask" else [int(re.findall(r"\d+", c[0])[0]), int(c[1])]
        for c in data
    ]
