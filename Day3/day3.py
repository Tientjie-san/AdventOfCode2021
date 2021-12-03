def get_input(file): 
    with open(file) as file_in:
        return [line.strip() for line in file_in]

puzzle_input = get_input("input.txt")

ones = 0
zeros = 0

gamma_rate = ""
epsilon_rate = ""

binary_length = len(puzzle_input[0])

for i in range(binary_length):
    count = 0
    for j in range(len(puzzle_input)):
        count += int(puzzle_input[j][i])
    if len(puzzle_input) - count < count:
       gamma_rate += "1"
    else:
        gamma_rate += "0" 

for char in gamma_rate:
    if char == "1":
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"

gamma_rate = int(gamma_rate,2)
epsilon_rate = int(epsilon_rate, 2)
print(gamma_rate * epsilon_rate)