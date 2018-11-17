import math
import numpy as np

with open(f"/home/kuro/Documents/Programming/CodingContest18/level3/level3_2.in", "r") as current_level:
    current_level.readline()
    for line in current_level:
        dataset = [int(i) for i in line.rstrip("\n").split(" ")]

        coord_a = [dataset[0], dataset[1]]
        coord_b = [dataset[2], dataset[3]]

        calc_range = np.linspace(0, 1, 10001)
        solutions = []
        for ratio in calc_range:
            distance_x = ((coord_b[0] - coord_a[0]) * ratio) + coord_a[0]
            distance_y = ((coord_b[1] - coord_a[1]) * ratio) + coord_a[1]
            solutions.append([int(round(distance_x)), int(round(distance_y))])
        thy_set = set(tuple(i) for i in solutions)
    

        with open(f"/home/kuro/Documents/Programming/CodingContest18/level3/level3_2.out", "a") as current_solution:
            for element in thy_set:
                current_solution.write(f"{element[0]} {element[1]} ")
            current_solution.write("\n")
