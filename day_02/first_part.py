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
    low = int(re.findall("\d+", policy)[0])
    high = int(re.findall("\d+", policy)[-1])
    letter = policy[-1]
    if (pw.count(letter) >= low) and (pw.count(letter) <= high):
        # print(f"VALID:\t{policy}\t{pw}\t (count is {pw.count(letter)})")
        return True
    else:
        # print(f"INVALID:\t{policy}\t{pw}\t (count is {pw.count(letter)})")
        return False


def count_valid(pass_list: list) -> int:
    return sum([check_one(*pol_pw) for pol_pw in pass_list])


# print(count_valid(TEST))
print(count_valid(INPUT))
