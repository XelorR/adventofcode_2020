import re

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


input_data = parse_raw(INPUT)
print("Answer is", count_in(input_data, "shiny gold") - 1)
