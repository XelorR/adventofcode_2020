INPUT = [int(i) for i in open("input.txt").readlines()]

for i in INPUT:
    for j in INPUT:
        for k in INPUT:
            if i + j + k == 2020:
                print(i * j * k)
                exit()
