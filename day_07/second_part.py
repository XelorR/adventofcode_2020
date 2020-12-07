import re
from pprint import pprint

EXAMPLE = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

with open("input.txt") as input_file:
    INPUT = input_file.read()


def parse_raw(data_raw: str) -> dict:
    data_list = data_raw.strip().split("\n")
    out = {}
    for row in data_list:
        current_bag, other_bags = row.split(" bags contain ")
        if other_bags == "no other bags.":
            out[current_bag] = {}
        else:
            out[current_bag] = {re.sub(r" bag.*$", "", bag)[2:]: int(
                re.sub(r" bag.*$", "", bag)[0]) for bag in
                other_bags.split(", ")}
    return out


def count_in(data: dict, looking_for: str):
    bag_count = 1
    for bag_type in data[looking_for]:
        bag_count += data[looking_for][bag_type] * count_in(data, bag_type)
    return bag_count


example_data = parse_raw(EXAMPLE)
input_data = parse_raw(INPUT)

pprint(example_data)
print("Answer is", count_in(input_data, "shiny gold") - 1)