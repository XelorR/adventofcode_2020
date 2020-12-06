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


def count_everyone_answers(single_group: list):
    first_member = set(single_group[0])
    if len(single_group) == 1:
        return len(first_member)
    else:
        for member in single_group[1:]:
            first_member = first_member & set(member)
        return len(first_member)


assert sum(count_everyone_answers(group) for group in parse_input(EXAMPLE)) == 6
print(sum(count_everyone_answers(group) for group in parse_input(INPUT)))
