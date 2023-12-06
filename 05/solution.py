def parse_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def process_seeds_and_blocks(input_text):
    blocks = input_text.split("\n\n")
    seeds, *block_texts = blocks
    seed_values = list(map(int, seeds.split(":")[1].split()))

    for block_text in block_texts:
        block_lines = block_text.splitlines()[1:]
        ranges = [list(map(int, line.split())) for line in block_lines]
        new_seeds = []
        for seed_value in seed_values:
            for start, end, offset in ranges:
                if end <= seed_value < end + offset:
                    new_seeds.append(seed_value - end + start)
                    break
            else:
                new_seeds.append(seed_value)
        seed_values = new_seeds

    return min(seed_values)

def process_inputs_and_blocks(input_text):
    blocks = input_text.split("\n\n")
    inputs, *block_texts = blocks
    input_values = list(map(int, inputs.split(":")[1].split()))
    seed_ranges = [(input_values[i], input_values[i] + input_values[i + 1]) for i in range(0, len(input_values), 2)]

    for block_text in block_texts:
        block_lines = block_text.splitlines()[1:]
        ranges = [list(map(int, line.split())) for line in block_lines]
        new_seeds = []
        while len(seed_ranges) > 0:
            seed_start, seed_end = seed_ranges.pop()
            for a, b, c in ranges:
                overlap_start = max(seed_start, b)
                overlap_end = min(seed_end, b + c)
                if overlap_start < overlap_end:
                    new_seeds.append((overlap_start - b + a, overlap_end - b + a))
                    if overlap_start > seed_start:
                        seed_ranges.append((seed_start, overlap_start))
                    if seed_end > overlap_end:
                        seed_ranges.append((overlap_end, seed_end))
                    break
            else:
                new_seeds.append((seed_start, seed_end))
        seed_ranges = new_seeds
    return min(seed_ranges)[0]

if __name__ == "__main__":
    filename = "in.txt"
    input_text = parse_file(filename)
    result_seeds_and_blocks = process_seeds_and_blocks(input_text)
    result_inputs_and_blocks = process_inputs_and_blocks(input_text)
    print("Part 1:", result_seeds_and_blocks)
    print("Part 2:", result_inputs_and_blocks)
