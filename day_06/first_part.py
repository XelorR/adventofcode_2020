with open("input.txt") as input_file:
    INPUT = input_file.read()

EXAMPLE = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def parse_input(raw_data: str) -> list:
    return [gr.split() for gr in raw_data.strip().split("\n\n")]


def count_unique_in_group(group: list) -> int:
    return len(set("".join(group)))


def sum_uniques(data: list) -> int:
    return sum(count_unique_in_group(gr) for gr in data)


assert sum_uniques(parse_input(EXAMPLE)) == 11
print(sum_uniques(parse_input(INPUT)))
