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

def count_trees(some_map: list, step_right: int, step_down: int) -> int:
    position_in_row = 0
    trees = 0

    for iter, row in enumerate(some_map):
        if iter % step_down == 0:
            if row[position_in_row % len(row)] == "#":
                trees += 1
            position_in_row += step_right

    return trees


def multiply_slopes(some_map: list) -> int:
    return (
        count_trees(some_map, 1, 1)
        * count_trees(some_map, 3, 1)
        * count_trees(some_map, 5, 1)
        * count_trees(some_map, 7, 1)
        * count_trees(some_map, 1, 2)
    )


print("Example map:", multiply_slopes(example_map), "in total")
print("My input map:", multiply_slopes(input_map), "in total")
