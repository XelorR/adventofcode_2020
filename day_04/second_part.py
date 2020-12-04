import re
from pprint import pprint

INVALID_IDS = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

VALID_IDS = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


def check_byr(value: str) -> bool:
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    """
    if re.match(r"\d{4}", value):
        return int(value) >= 1920 and int(value) <= 2002
    else:
        return False


def check_iyr(value: str) -> bool:
    """
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    if re.match(r"\d{4}", value):
        return int(value) >= 2010 and int(value) <= 2020
    else:
        return False


def check_eyr(value: str) -> bool:
    """
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    """
    if re.match(r"\d{4}", value):
        return int(value) >= 2020 and int(value) <= 2030
    else:
        return False


def check_hgt(value: str) -> bool:
    """
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """
    number = int(re.findall(r"\d+", value)[0])
    return (bool(re.match(r"\d+in", value)) and number >= 59 and number <= 76) or (
        bool(re.match(r"\d+cm", value)) and number >= 150 and number <= 193
    )


def check_hcl(value: str) -> bool:
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    return bool(re.match(r"#[0-9a-f]", value))


def check_ecl(value: str) -> bool:
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(value: str) -> bool:
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    return bool(re.match(r"^\d{9}$", value))


def validate_id(id: dict) -> bool:
    if (
        "pid" in id
        and "byr" in id
        and "ecl" in id
        and "eyr" in id
        and "hcl" in id
        and "hgt" in id
        and "iyr" in id
    ):
        if (
            check_pid(id["pid"])
            and check_byr(id["byr"])
            and check_ecl(id["ecl"])
            and check_eyr(id["eyr"])
            and check_hcl(id["hcl"])
            and check_hgt(id["hgt"])
            and check_iyr(id["iyr"])
        ):
            print("\nValid:")
            pprint(id)
            return True
        else:
            print("\nInvalid:")
            pprint(id)
            return False
    else:
        print("\nInvalid:")
        pprint(id)
        return False


def count_valid(data: list) -> int:
    return sum([validate_id(id) for id in data])


def parse_raw(raw_data: str) -> list:
    return [
        {field.split(":")[0]: field.split(":")[-1] for field in id.split()}
        for id in raw_data.rstrip().split("\n\n")
    ]


assert check_byr("2002")
assert ~check_byr("2003")
assert check_hgt("60in")
assert check_hgt("190cm")
assert ~check_hgt("190in")
assert ~check_hgt("190")
assert check_hcl("#123abc")
assert ~check_hcl("#123abz")
assert ~check_hcl("123abz")
assert check_ecl("brn")
assert ~check_ecl("wat")
assert check_pid("000000001")
assert ~check_pid("0123456789")
assert sum([validate_id(id) for id in parse_raw(VALID_IDS)]) == 4
assert sum([validate_id(id) for id in parse_raw(INVALID_IDS)]) == 0
assert count_valid(parse_raw(VALID_IDS)) == 4
assert count_valid(parse_raw(INVALID_IDS)) == 0


if __name__ == "__main__":
    INPUT = open("input.txt").read()
    input_data = parse_raw(INPUT)
    print("\nTotal number of valid ids is", count_valid(input_data))
    # it should be 167!
    # but my result is 168...
