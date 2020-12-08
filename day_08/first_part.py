from pprint import pprint

with open("input.txt", "r") as input_file:
    INPUT = input_file.read().strip()

EXAMPLE = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def parse_raw(data_raw: str) -> list:
    return [[row.split()[0], int(row.split()[1])] for row in data_raw.splitlines()]


example_data = parse_raw(EXAMPLE)
input_data = parse_raw(INPUT)

pprint(example_data)
