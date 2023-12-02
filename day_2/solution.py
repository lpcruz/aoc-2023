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

def calculate_game_value(game_line):
    blues, reds, greens = [], [], []
    colors = game_line.split(': ')[1]
    draws = colors.split('; ')
    
    for draw in draws:
        color_list = draw.split(', ')
        for item in color_list:
            number, color = item.split(' ')
            if color == 'blue':
                blues.append(int(number))
            elif color == 'red':
                reds.append(int(number))
            elif color == 'green':
                greens.append(int(number))
    
    return max(reds) * max(greens) * max(blues)

def main(filename):
    with open(filename, "r") as file:
        puzzle_input = file.read().strip().split('\n')

    red_max = 12
    green_max = 13
    blue_max = 14

    # Part One
    value = sum(idx + 1 for idx, line in enumerate(puzzle_input) if calculate_value(line, red_max, green_max, blue_max))
    print("Sum of IDs of possible games (Part One):", value)

    # Part Two
    game_values = [calculate_game_value(line) for line in puzzle_input]
    total_value = sum(game_values)
    print("Sum of game values (Part Two):", total_value)

if __name__ == "__main__":
    main("in.txt")
