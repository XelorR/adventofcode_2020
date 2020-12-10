EXAMPLE = ("16\n"
           "10\n"
           "15\n"
           "5\n"
           "1\n"
           "11\n"
           "7\n"
           "19\n"
           "6\n"
           "12\n"
           "4")

LARGER_EXAMPLE = ("28\n"
                  "33\n"
                  "18\n"
                  "42\n"
                  "31\n"
                  "14\n"
                  "46\n"
                  "20\n"
                  "48\n"
                  "47\n"
                  "24\n"
                  "23\n"
                  "49\n"
                  "45\n"
                  "19\n"
                  "38\n"
                  "39\n"
                  "11\n"
                  "1\n"
                  "32\n"
                  "25\n"
                  "35\n"
                  "8\n"
                  "17\n"
                  "7\n"
                  "9\n"
                  "4\n"
                  "2\n"
                  "34\n"
                  "10\n"
                  "3")

with open("input.txt", "r") as input_file:
    INPUT = input_file.read().strip()


def parse_raw(raw_data: str) -> list:
    return [int(adapter) for adapter in raw_data.strip().splitlines()]


def part_one_diff_counts(raw_data: str) -> dict:
    data = sorted(parse_raw(raw_data))
    full_data = [0] + data + [(max(data) + 3)]
    diffs = {}
    for i, e in enumerate(full_data[1:]):
        diff = e - full_data[i]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
    return diffs


assert part_one_diff_counts(EXAMPLE) == {1: 7, 3: 5}
assert part_one_diff_counts(LARGER_EXAMPLE) == {1: 22, 3: 10}

counts = part_one_diff_counts(INPUT)
print("Part one answer is:", counts[1] * counts[3])
