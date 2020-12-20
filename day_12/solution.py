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
        self.data = (re.findall(r"([A-Z]+)(\d+)", comm)[0] for comm in
                     raw_data.splitlines())
        self.directions = ["N", "E", "S", "W"]
        self.facing = facing
        self.facing_index = [i for i, d in enumerate(self.directions) if d == facing][0]
        self.coordinates_xy = [0, 0]
        self.movements = {
            "E": self.__move_east,
            "W": self.__move_west,
            "N": self.__move_north,
            "S": self.__move_south,
        }

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
        self.movements[comm](units)

    def move_full_path(self):
        for command in self.data:
            if command[0] in "NWSE":
                self.move(command)
            elif command[0] in "FB":
                self.move((self.facing, command[1]))
            elif command[0] in "LR":
                self.rotate(command)
            print(command, self.coordinates_xy)

    def rotate(self, command: tuple):
        comm = command[0]
        degrees = int(command[1])
        step = degrees // 90
        self.facing_index = (self.facing_index + step) % 4
        self.facing = self.directions[self.facing_index]


example_ship = Ship(EXAMPLE)
example_ship.move_full_path()
x, y = example_ship.coordinates_xy
assert abs(x) + abs(y) == 25

input_ship = Ship(INPUT)
input_ship.move_full_path()
x, y = input_ship.coordinates_xy
print("Manhattan distance from initial position is", abs(x) + abs(y),
      "(part one solution)")
