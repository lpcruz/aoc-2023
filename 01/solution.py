import re

def parse_input_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def part_one(lines):
    total_sum = 0

    for line in lines:
        digits = [ch for ch in line if ch.isdigit()]
        if digits:
            total_sum += int(digits[0] + digits[-1])
    return total_sum

def part_two(lines):
    total_sum = 0
    n = "one two three four five six seven eight nine".split()
    p = "(?=(" + "|".join(n) + "|\\d))"

    def index(x):
        if x in n:
            return str(n.index(x) + 1)
        return x

    for line in lines:
        digits = [*map(index, re.findall(p, line))]
        total_sum += int(digits[0] + digits[-1])
    return total_sum

file_contents = parse_input_file('in.txt')
part_one_result = part_one(file_contents)
part_two_result = part_two(file_contents)

print(part_one_result)
print(part_two_result)
