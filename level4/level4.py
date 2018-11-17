import numpy as np
import math
levels = [1]

for level in levels:
    with open(f"/home/kuro/Documents/Programming/CodingContest18/level4/level4_{level}.in", "r") as current_level:
        current_level.readline()

        level_input = []
        for line in current_level:
            level_input.append([int(a) for a in line.rstrip("\n").split(" ")])

        coord_list = []

        for index_row, row in enumerate(level_input):
            for index_element, element in enumerate(row):
                if index_row == 0 and index_element == 0:
                    if element != 0:
                        coord_list.append([index_row, index_element])
                elif index_row == 0:
                    if element != 0 and level_input[index_row][index_element - 1] != element:
                        coord_list.append([index_row, index_element])

                elif index_element == 0:
                    if element != 0 and level_input[index_row - 1][index_element] != element:
                        coord_list.append([index_row, index_element])

                else:
                    if element != 0 and level_input[index_row - 1][index_element] != element and level_input[index_row][index_element - 1] != element:
                        coord_list.append([index_row, index_element])

        solutions = {}

        for index, coords in enumerate(coord_list):
            row, element = coords
            len_counter = 0
            value_to_compare = level_input[row][element]
            while level_input[row][element + len_counter] == value_to_compare:
                len_counter += 1

            solutions[index] = {
                "coords": coord_list[index], "length": len_counter}

        for index, coords in enumerate(coord_list):
            row, element = coords
            len_counter = 0
            value_to_compare = level_input[row][element]
            while level_input[row + len_counter][element] == value_to_compare:
                len_counter += 1
            solutions[index]["height"] = len_counter

        keys_to_pop = []
        for key, value in solutions.items():
            if value["length"] <= 3 or value["height"] <= 3:
                keys_to_pop.append(key)

        for key in keys_to_pop:
            solutions.pop(key)
        with open(f"/home/kuro/Documents/Programming/CodingContest18/level4/level4_{level}.out", "a") as current_solution:
            for index, value in enumerate(solutions):
                print(f"index: {index}  value: {value}")
                x_offset = solutions[value]["coords"][0] + math.floor(solutions[value]["length"] / 2)
                y_offset = solutions[value]["coords"][1] + math.floor(solutions[value]["height"] / 2)
                current_solution.write(f"{index} {x_offset} {y_offset} ")
