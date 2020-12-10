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


def find_first_error(data_raw, length_to_check=5):
    for index, elem in enumerate(parse_raw(data_raw)[length_to_check:]):
        prev_five = parse_raw(data_raw)[index: index + length_to_check]
        check = False
        for i, a in enumerate(prev_five):
            for j, b in enumerate(prev_five):
                if i != j and a + b == elem:
                    check = True
        if not check:
            return elem


assert find_first_error(EXAMPLE) == 127
print(find_first_error(INPUT, 25))
