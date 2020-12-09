with open("input.txt", "r") as input_file:
    INPUT = input_file.read().strip()

EXAMPLE = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def parse_raw(data_raw: str) -> list:
    return [int(e) for e in data_raw.splitlines()]
