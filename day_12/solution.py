import re

EXAMPLE = """F10
N3
F7
R90
F11"""

with open("input.txt", "r") as input_file:
    INPUT = input_file.read().strip()


class Ship:
    def __init__(self, raw_data: str):
        self.data = (re.findall(r"(\w+)(\d+)", comm)[0] for comm in raw_data.splitlines())


example_ship = Ship(EXAMPLE)
