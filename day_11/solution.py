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

    def __get_seats_left(self, row: int, column: int) -> list:
        if column <= 8:
            return self.data[row][:column]
        else:
            return self.data[row][column - 8:column]

    def __get_seats_right(self, row: int, column: int) -> list:
        if self.width - column <= 9:
            return self.data[row][column + 1:]
        else:
            return self.data[row][column + 1:column + 9]
