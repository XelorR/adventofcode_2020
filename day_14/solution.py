import re
from pprint import pprint

EXAMPLE = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

with open("input.txt") as f:
    INPUT = f.read().strip()


class Decoder:

    def __init__(self, data_raw: str):
        self.program = self.parse_raw(data_raw)
        self.memory = {}

    def parse_raw(self, data_raw: str):
        data = [c.split(" = ") for c in data_raw.splitlines()]
        return [
            c if c[0] == "mask" else [int(re.findall(r"\d+", c[0])[0]), int(c[1])]
            for c in data
        ]

    def print_state(self):
        pprint(example_decoder.program)
        pprint(example_decoder.memory)


example_decoder = Decoder(EXAMPLE)
example_decoder.print_state()
