import re;

def part_one(filename):
    total_sum = 0

    for line in open(filename):
        digits = [ch for ch in line if ch.isdigit()]
        if digits:
            total_sum += int(digits[0] + digits[-1])
    return total_sum


def part_two(filename):
    total_sum = 0
    n = "one two three four five six seven eight nine".split()
    p = "(?=(" + "|".join(n) + "|\\d))"

    def index(x):
        if x in n:
            return str(n.index(x) + 1)
        return x

    for line in open(filename):
        digits = [*map(index, re.findall(p,line))]
        total_sum += int(digits[0] + digits[-1])
    return total_sum

part_one_result = part_one('in.txt')
part_two_result = part_two('in.txt')
print(part_one_result)
print(part_two_result)
