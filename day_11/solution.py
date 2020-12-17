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
    data: list
    width: int
    length: int
    occupied: int

    def __init__(self, data_raw: str):
        self.data = [[position for position in row] for row in data_raw.splitlines()]
        self.width = len(self.data[0])
        self.length = len(self.data)
        self.occupied = 0

    def count_occupied_adjacent_seats(self, row: int, column: int) -> int:
        data = chain(*[seat[max([0, column - 1]):min(self.width, column + 2)] for seat in
                       self.data[max([0, row - 1]):min(self.length, row + 2)]])
        return sum(s == "#" for s in data) - int(self.data[row][column] == "#")

    def switch_seats(self):
        while True:
            data_current = deepcopy(self.data)
            for i, row in enumerate(self.data):
                for j, seat in enumerate(row):
                    occupied_nearby = self.count_occupied_adjacent_seats(i, j)
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


def get_diagonal(list_of_lists: list):
    return [elem[i] for i, elem in enumerate(list_of_lists) if
            i < min([len(list_of_lists), len(list_of_lists[0])])]


class FerryPartTwo(Ferry):

    def count_occupied_adjacent_seats(self, row: int, column: int) -> int:
        horizontal = [s for i, s in enumerate(self.data[row]) if i != column]
        vertical = [s[column] for i, s in enumerate(self.data) if i != row]

        up = vertical[:row].reverse()
        down = vertical[row:] if row < len(vertical) else []
        left = horizontal[:column].reverse()
        right = horizontal[column:] if column < len(horizontal) else []

        up_left = get_diagonal([reversed(r[:column]) for r in reversed(
            self.data[:row])]) if column > 0 and row > 0 else []
        up_right = get_diagonal([r[column + 1] for r in reversed(
            self.data[:row])]) if column + 1 < self.width and row > 0 else []
        down_left = get_diagonal(
            [reversed(r[:column]) for r in
             self.data[row + 1:]]) if column > 0 and self.length > row + 1 else []
        down_right = get_diagonal([r[column + 1:] for r in
                                   self.data[
                                   row + 1:]]) if self.length > row + 1 and column + 1 < self.width else []


example_ferry = Ferry(EXAMPLE)
example_ferry.switch_seats()
assert example_ferry.occupied == 37

input_ferry = Ferry(INPUT)
input_ferry.switch_seats()
print("There are", input_ferry.occupied,
      "occupied seats in our input ferry (part one solution)")
