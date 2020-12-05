with open("input.txt") as f:
    INPUT = [row.rstrip() for row in f.readlines()]

low = 0
high = 127
for index, letter in enumerate("FBFBBFFRLR"):
    print(low, high)
    if letter == "F":
        high = (high - low) // 2 + low
    elif letter == "B":
        low = (high - low) // 2 + low + 1
    elif letter == "L":
        pass
    elif letter == "R":
        pass
