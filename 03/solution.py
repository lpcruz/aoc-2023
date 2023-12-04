import re

def is_adjacent_to_obstacle(schematic, row, col):
    for d_row in range(-1, 2):
        for d_col in range(-1, 2):
            if d_row == 0 and d_col == 0:
                continue
            new_row, new_col = row + d_row, col + d_col
            if 0 <= new_row < len(schematic) and 0 <= new_col < len(schematic[new_row]):
                if schematic[new_row][new_col] not in '.0123456789':
                    return True
    return False

def calculate_sum_of_parts(schematic):
    total_sum_of_parts = 0
    for row, line in enumerate(schematic):
        for match in re.finditer(r'\d+', line):
            part_number = int(match.group())
            start, end = match.start(), match.end()
            if any(is_adjacent_to_obstacle(schematic, row, col) for col in range(start, end)):
                total_sum_of_parts += part_number
    return total_sum_of_parts

def calculate_sum_of_gears(schematic):
    total_sum_of_gears = 0

    number_positions = []
    for row, line in enumerate(schematic):
        number_positions.append([])
        for match in re.finditer(r'\d+', line):
            number_positions[row].append((int(match.group()), match.start(), match.end() - 1))

    for row, line in enumerate(schematic):
        for match in re.finditer(r'\*', line):
            col_position = match.start()
            adjacent_parts = set()
            prod_adjacent_parts = 1
            for d_row in range(-1, 2):
                for d_col in range(-1, 2):
                    if d_row == 0 and d_col == 0:
                        continue
                    new_row, new_col = row + d_row, col_position + d_col
                    if 0 <= new_row < len(schematic):
                        for num, start, end in number_positions[new_row]:
                            if start <= new_col <= end:
                                adjacent_parts.add(num)
            
            if len(adjacent_parts) == 2:
                prod_adjacent_parts = adjacent_parts.pop() * adjacent_parts.pop()
                total_sum_of_gears += prod_adjacent_parts
    return total_sum_of_gears
                   
with open("in.txt") as file_handle:
    schematic_data = file_handle.read().splitlines()

print(calculate_sum_of_parts(schematic_data), calculate_sum_of_gears(schematic_data))
