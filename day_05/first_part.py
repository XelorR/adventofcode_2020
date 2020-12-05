with open("input.txt") as f:
    INPUT = [row.rstrip() for row in f.readlines()]

low = 0
high = 127
left = 0
right = 7
for index, letter in enumerate("FBFBBFFRLR"):
    if letter == "F":
        high = (high - low) // 2 + low
    elif letter == "B":
        low = (high - low) // 2 + low + 1
    elif letter == "L":
        right = (right - left) // 2 + left
    elif letter == "R":
        left = (right - left) // 2 + left + 1
    print(letter, low, high, left, right)
decoded = high * 8 + right
print("Decoded:", decoded)
