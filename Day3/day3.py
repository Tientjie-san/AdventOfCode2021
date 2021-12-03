def get_input(file): 
    with open(file) as file_in:
        return [line.strip() for line in file_in]

puzzle_input = get_input("input.txt")

def most_occured_bit(pos, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i][pos] == '1':
            count += 1
    
    if len(arr) - count <= count:
        return "1"
    else:
        return "0" 

binary_length = len(puzzle_input[0])
puzzle_input_copy_oxygen = puzzle_input[:]
puzzle_input_copy_co2 = puzzle_input[:]

for i in range(binary_length):
    count = 0
    
    if len(puzzle_input_copy_oxygen) != 1:
        most_occuring_oxy = most_occured_bit(i, puzzle_input_copy_oxygen)
        puzzle_input_copy_oxygen = [number for number in puzzle_input_copy_oxygen if number[i] == most_occuring_oxy]

    if len(puzzle_input_copy_co2) != 1:
        most_occuring_co2 = most_occured_bit(i, puzzle_input_copy_co2)
        puzzle_input_copy_co2 = [number for number in puzzle_input_copy_co2 if number[i] != most_occuring_co2]

oxigen_rating = puzzle_input_copy_oxygen[0]
co2_rating = puzzle_input_copy_co2[0]


oxigen_rating = int(oxigen_rating,2)
co2_rating = int(co2_rating, 2)

print(oxigen_rating * co2_rating)