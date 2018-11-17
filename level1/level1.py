import numpy as np

levels = [0,1,2,3]

for level in levels:
    with open(f"/home/kuro/Documents/Programming/CodingContest18/level1/level1_{level}.in", "r") as current_level:
        current_level.readline();

        new_list = []
        for line in current_level:
            new_list.append([int(a) for a in line.rstrip("\n").split(" ")])

        sizes = []
        for element in new_list:
            sizes += element

        stripped_sizes = list(filter(lambda x: x > 0, sizes))

        solution = list(set(stripped_sizes))

        solution.sort()

        if solution == []:
            solution = [0]
        print(" ".join(map(str, solution)))