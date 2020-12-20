import re

EXAMPLE = """F10
N3
F7
R90
F11"""

with open("input.txt", "r") as input_file:
    INPUT = input_file.read().strip()


class Ship:
    def __init__(self, raw_data: str, facing: str = "E"):
        self.data = (re.findall(r"(\w+)(\d+)", comm)[0] for comm in raw_data.splitlines())
        self.facing = facing
        self.coordinates_xy = [0, 0]

    def __move_east(self, units: int):
        self.coordinates_xy[1] += units

    def __move_west(self, units: int):
        self.coordinates_xy[1] -= units

    def __move_north(self, units: int):
        self.coordinates_xy[0] += units

    def __move_south(self, units: int):
        self.coordinates_xy[0] -= units

    def move(self, command: tuple):
            comm = command[0]
            units = int(command[1])

    def rotate(self, command: tuple):
        comm = command[0]
        units = int(command[1])


example_ship = Ship(EXAMPLE)
print(list(example_ship.data))
