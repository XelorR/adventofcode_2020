input_map = open("input.txt").read()

example_map = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def calculate_expand(input_map: str) -> int:
    return int(len(input_map.split("\n")) / (len(input_map.split("\n")[0]) // 3 + 1))


def expand_once(input_map: str) -> str:
    return "\n".join(r + r for r in input_map.split("\n"))


def expand_a_lot(input_map: str) -> str:
    for i in range(calculate_expand(input_map)):
        input_map = expand_once(input_map)
    return input_map


def go_go_go(map: str) -> int:

    map = map.split("\n")
    position_in_row = 0
    trees = 0
    temp_row = []
    mark = "O"

    for iter, row in enumerate(map):
        if map[iter][position_in_row] == "#":
            trees += 1
            mark = "X"
        else:
            mark = "O"
        temp_row = [c for c in map[iter]]
        temp_row[position_in_row] = mark
        print("".join(temp_row))

        position_in_row += 3

    print("trees met: ", trees, "\n")
    return trees


example_map = expand_a_lot(example_map)
input_map = expand_a_lot(input_map)

go_go_go(example_map)
go_go_go(input_map)
