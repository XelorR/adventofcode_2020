import re


INPUT = [
    [s.split(": ")[0], s.split(": ")[-1].rstrip()]
    for s in open("input.txt").readlines()
]

TEST = [
    ["1-3 a", "abcde"],
    ["1-3 b", "cdefg"],
    ["2-9 c", "ccccccccc"],
]


def check_one(policy: str, pw: str) -> bool:
    first = int(re.findall("\d+", policy)[0])
    second = int(re.findall("\d+", policy)[-1])
    letter = policy[-1]
    if sum([pw[first - 1] == letter, pw[second - 1] == letter]) == 1:
        # print(f"VALID:\t{policy}\t{pw}")
        return True
    else:
        # print(f"INVALID:\t{policy}\t{pw}")
        return False


def count_valid(pass_list: list) -> int:
    return sum([check_one(*pol_pw) for pol_pw in pass_list])


# print(count_valid(TEST))
print(count_valid(INPUT))
