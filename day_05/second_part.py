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


def generate_fullist():
    pass
