def get_input(file): 
    with open(file) as file_in:
        return [int(line.strip()) for line in file_in]

puzzle_input = get_input("input.txt")

count = 0
for i in range(1, len(puzzle_input)-2):
    previous_total = puzzle_input[i-1] + puzzle_input[i] + puzzle_input[i+1]
    current_total = puzzle_input[i] + puzzle_input[i+1] + puzzle_input[i+2]

    if previous_total < current_total:
        count += 1

print(count)
