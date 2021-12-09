puzzle_input = []
with open("input.txt") as my_file:
    for line in my_file:
        line = line.strip().split(",")
        for num in line:
            puzzle_input.append(int(num))

# for min crab pos to max crab pos, calculate distance of pos to all crab pos, store minimum pos if distance is loweest

min_distance = 100000000000000
for i in range(min(puzzle_input), max(puzzle_input)+1):
    total_distance = 0
    for crab_pos in puzzle_input:
        for j in range(1, abs(crab_pos - i) + 1):
            total_distance += j
    if total_distance < min_distance:
        min_distance = total_distance

print(min_distance)

