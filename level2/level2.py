import math

with open(f"/home/kuro/Documents/Programming/CodingContest18/level2/level2_3.in", "r") as current_level:
    current_level.readline()
    for line in current_level:
        dataset = [float(i) for i in line.rstrip("\n").split(" ")]

        coord_a = [dataset[0], dataset[1]]
        coord_b = [dataset[2], dataset[3]]
        ratio = dataset[4]

        distance_x = ((coord_b[0] - coord_a[0]) * ratio) + coord_a[0]
        distance_y = ((coord_b[1] - coord_a[1]) * ratio) + coord_a[1]

        print(distance_x, distance_y)

        with open(f"/home/kuro/Documents/Programming/CodingContest18/level2/level2_3.out", "a") as current_solution:
            current_solution.write(f"{int(round(distance_x))} {int(round(distance_y))}\n")
