INPUT = open("input.txt").read()

EXAMPLE = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


EXPECTED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
]


def parse_raw(raw_data: str) -> list:
    return [
        {field.split(":")[0]: field.split(":")[-1] for field in id.split()}
        for id in raw_data.rstrip().split("\n\n")
    ]


input_data = parse_raw(INPUT)
example_data = parse_raw(EXAMPLE)


def count_valid(data: list) -> int:
    return sum(
        [
            sum([key in EXPECTED_FIELDS for key in id]) == len(EXPECTED_FIELDS)
            for id in data
        ]
    )


print(count_valid(example_data))
print(count_valid(input_data))
