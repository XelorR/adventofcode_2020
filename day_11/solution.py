from pprint import pprint

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

    def get_seats_left(self, row: int, column: int) -> list:
        if column <= 8:
            return self.data[row][:column]
        else:
            return self.data[row][column - 8:column]

    def get_seats_right(self, row: int, column: int) -> list:
        if self.width - column <= 9:
            return self.data[row][column + 1:]
        else:
            return self.data[row][column + 1:column + 9]

    def get_seats_up(self, row: int, column: int) -> list:
        if row <= 8:
            return [seat[column] for seat in self.data[:row]]
        else:
            return [seat[column] for seat in self.data[row - 8:row]]

    def get_seats_down(self, row: int, column: int) -> list:
        if self.length - row <= 9:
            return [seat[column] for seat in self.data[row + 1:]]
        else:
            return [seat[column] for seat in self.data[row + 1:row + 9]]


example_ferry = Ferry(EXAMPLE)
pprint(example_ferry.data)
print(example_ferry.get_seats_up(row=9, column=9))
