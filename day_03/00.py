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

example_map = example_map.split("\n")
input_map = input_map.split("\n")

position_in_row = 0
trees = 0

for row in example_map:
    if row[position_in_row % len(row)] == "#":
        trees += 1
    position_in_row += 3

print(trees)
