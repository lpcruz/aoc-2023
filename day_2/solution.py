def calculate_value(line, red_max, green_max, blue_max):
    colors = line.split(': ')[1]
    subsets = colors.split('; ')
    blues, reds, greens = [], [], []
    
    for subset in subsets:
        color_list = subset.split(', ')
        for item in color_list:
            number, color = item.split(' ')
            if color == 'blue':
                blues.append(int(number))
            elif color == 'red':
                reds.append(int(number))
            elif color == 'green':
                greens.append(int(number))
    
    if max(reds) <= red_max and max(greens) <= green_max and max(blues) <= blue_max:
        return True
    return False

def part_one(filename):
    with open(filename, "r") as file:
        puzzle_input = file.read().strip().split('\n')
    red_max = 12
    green_max = 13
    blue_max = 14
    value = sum(idx + 1 for idx, line in enumerate(puzzle_input) if calculate_value(line, red_max, green_max, blue_max))
    return value

result = part_one("in.txt")
print("Sum of IDs of possible games:", result)
