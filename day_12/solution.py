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
        self.data = (
            re.findall(r"([A-Z]+)(\d+)", comm)[0] for comm in raw_data.splitlines()
        )
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
        self.coordinates_xy[0] += units

    def __move_west(self, units: int):
        self.coordinates_xy[0] -= units

    def __move_north(self, units: int):
        self.coordinates_xy[1] += units

    def __move_south(self, units: int):
        self.coordinates_xy[1] -= units

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
            print(command, self.coordinates_xy, self.facing)

    def rotate(self, command: tuple):
        comm = command[0]
        degrees = int(command[1])
        step = degrees // 90
        self.facing_index = (
            (self.facing_index + step) % 4
            if comm == "R"
            else (self.facing_index - step) % 4
        )
        self.facing = self.directions[self.facing_index]


class ShipToWaypoint(Ship):

    def __init__(self, raw_data: str, facing: str = "E"):
        super().__init__(raw_data, facing)
        self.waypoint = [10, 1]
        self.waypoint_movements = {
            "E": self.__move_waypoint_east,
            "W": self.__move_waypoint_west,
            "N": self.__move_waypoint_north,
            "S": self.__move_waypoint_south,
        }

    def move_ship(self, command: tuple):
        n_times = int(command[1])
        relative_x = (self.waypoint[0] - self.coordinates_xy[0]) * n_times
        relative_y = (self.waypoint[1] - self.coordinates_xy[1]) * n_times
        self.coordinates_xy[0] += relative_x
        self.coordinates_xy[1] += relative_y
        self.waypoint[0] += relative_x
        self.waypoint[1] += relative_y

    def __move_waypoint_east(self, units: int):
        self.waypoint[0] += units

    def __move_waypoint_west(self, units: int):
        self.waypoint[0] -= units

    def __move_waypoint_north(self, units: int):
        self.waypoint[1] += units

    def __move_waypoint_south(self, units: int):
        self.waypoint[1] -= units

    def move_waypoint(self, command: tuple):
        comm = command[0]
        units = int(command[1])
        self.waypoint_movements[comm](units)

    def rotate_simple_case(self, direction: str, x: int, y: int):
        """
        Rotates one pair of coordinates around (0, 0)
        Always rotates 90 degrees left or right, depending on current self.facing
        """
        if self.facing == "N" and direction == "R":
            return y, x
        elif self.facing == "N" and direction == "L":
            return -y, x
        elif self.facing == "W" and direction == "R":
            return y, -x
        elif self.facing == "W" and direction == "L":
            return y, x
        elif self.facing == "S" and direction == "R":
            return y, x
        elif self.facing == "S" and direction == "L":
            return -y, x
        elif self.facing == "E" and direction == "R":
            return y, -x
        elif self.facing == "E" and direction == "L":
            return y, x

    def rotate(self, command: tuple):
        """
        rotates WAYPOINT instead of ship
        """
        comm = command[0]
        degrees = int(command[1])

        for _ in range(90 // degrees):
            relative_x = self.waypoint[0] - self.coordinates_xy[0]
            relative_y = self.waypoint[1] - self.coordinates_xy[1]
            relative_x, relative_y = self.rotate_simple_case(comm, relative_x, relative_y)

            # converting relative coordinates back to absolute
            self.waypoint[0] = relative_x + self.coordinates_xy[0]
            self.waypoint[1] = relative_y + self.coordinates_xy[1]

            self.facing_index = (
                (self.facing_index + 1) % 4
                if comm == "R"
                else (self.facing_index - 1) % 4
            )
            self.facing = self.directions[self.facing_index]

    def move_full_path(self):
        for command in self.data:
            if command[0] in "NWSE":
                self.move_waypoint(command)
            elif command[0] in "FB":
                self.move_ship((self.facing, command[1]))
            elif command[0] in "LR":
                self.rotate(command)
            print(command, self.coordinates_xy, self.waypoint, self.facing)


print("Part one")
example_ship = Ship(EXAMPLE)
example_ship.move_full_path()
x, y = example_ship.coordinates_xy
assert abs(x) + abs(y) == 25

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

input_ship = Ship(INPUT)
input_ship.move_full_path()
x, y = input_ship.coordinates_xy
print(
    "Manhattan distance from initial position is",
    abs(x) + abs(y),
    "(part one solution)",
)

print("\nPart two")
example_ship_part_two = ShipToWaypoint(EXAMPLE)
example_ship_part_two.move_full_path()
x, y = example_ship_part_two.coordinates_xy
print(abs(x) + abs(y))
