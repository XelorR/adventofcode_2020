with open("input.txt") as f:
    INPUT = [row.rstrip() for row in f.readlines()]


def decode_ticket(ticket: str) -> int:
    low = 0
    high = 127
    left = 0
    right = 7

    for index, letter in enumerate(ticket):
        if letter == "F":
            high = (high - low) // 2 + low
        elif letter == "B":
            low = (high - low) // 2 + low + 1
        elif letter == "L":
            right = (right - left) // 2 + left
        elif letter == "R":
            left = (right - left) // 2 + left + 1
    return high * 8 + right


assert decode_ticket("FBFBBFFRLR") == 357
assert decode_ticket("BFFFBBFRRR") == 567
assert decode_ticket("FFFBBBFRRR") == 119
assert decode_ticket("BBFFBBFRLL") == 820

print(max([decode_ticket(t) for t in INPUT]))
