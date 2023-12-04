def parse_file(file_path):
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.split(':')[1].strip()
            winning_numbers, all_numbers = [list(map(int, numbers.split())) for numbers in line.split(' | ')]
            data.append((winning_numbers, all_numbers))

    return data

def calculate_winnings(data):
    total_winnings = 0

    for winning_numbers, all_numbers in data:
        matching_numbers_count = sum(number in winning_numbers for number in all_numbers)
        if matching_numbers_count > 0:
            total_winnings += 2 ** (matching_numbers_count - 1)

    return total_winnings

def calculate_scratchcards(data):
    m = {}

    for idx, (winning_numbers, all_numbers) in enumerate(data):
        if idx not in m:
            m[idx] = 1

        matching_numbers_count = sum(number in winning_numbers for number in all_numbers)

        for n in range(idx + 1, idx + matching_numbers_count + 1):
            m[n] = m.get(n, 1) + m[idx]

    return sum(m.values())

file = parse_file('in.txt')
print('part one:', calculate_winnings(file))
print('part two:', calculate_scratchcards(file))
