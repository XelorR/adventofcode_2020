INPUT = [int(i) for i in open("input.txt").readlines()]

for i in INPUT:
    for j in INPUT:
        if i + j == 2020:
            print(i * j)
            exit()
