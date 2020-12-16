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

    def count_adjacent_seats(self, row: int, column: int) -> int:
        data = chain(*[seat[max([0, column - 1]):min(self.width, column + 2)] for seat in
                       self.data[max([0, row - 1]):min(self.length, row + 2)]])
        return sum(s == "#" for s in data) - int(self.data[row][column] == "#")
