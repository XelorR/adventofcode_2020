from copy import deepcopy
from itertools import chain

EXAMPLE = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

with open("input.txt") as input_file:
    INPUT = input_file.read().strip()


class Ferry:
    def __init__(self, data_raw: str):
        self.data = [[position for position in row] for row in data_raw.splitlines()]
        self.width = len(self.data[0])
        self.length = len(self.data)
        self.occupied = 0

    def count_adjacent_seats(self, row: int, column: int) -> int:
        data = chain(*[seat[max([0, column - 1]):min(self.width, column + 2)] for seat in
                       self.data[max([0, row - 1]):min(self.length, row + 2)]])
        return sum(s == "#" for s in data) - int(self.data[row][column] == "#")

    def switch_seats(self):
        while True:
            data_current = deepcopy(self.data)
            for i, row in enumerate(self.data):
                for j, seat in enumerate(row):
                    occupied_nearby = self.count_adjacent_seats(i, j)
                    if occupied_nearby == 0 and seat == "L":
                        data_current[i][j] = "#"
                    elif occupied_nearby >= 4 and seat == "#":
                        data_current[i][j] = "L"
            if data_current != self.data:
                self.data = deepcopy(data_current)
                self.occupied = sum(s == "#" for s in chain(*self.data))
            else:
                self.occupied = sum(s == "#" for s in chain(*self.data))
                break


example_ferry = Ferry(EXAMPLE)
example_ferry.switch_seats()
assert example_ferry.occupied == 37
