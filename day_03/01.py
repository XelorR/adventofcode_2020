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


print("Example map:", count_trees(example_map, step_right=3, step_down=1), "met")
print("My input map:", count_trees(input_map, step_right=3, step_down=1), "met")
