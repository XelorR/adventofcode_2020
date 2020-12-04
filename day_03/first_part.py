input_map = open("input.txt").read().rstrip()

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

def count_trees(some_map: list) -> int:
    position_in_row = 0
    trees = 0

    for row in some_map:
        if row[position_in_row % len(row)] == "#":
            trees += 1
        position_in_row += 3

    return trees

print("Example map:", count_trees(example_map), "met")
print("My input map:", count_trees(input_map), "met")
