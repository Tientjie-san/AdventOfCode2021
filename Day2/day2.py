def get_input(file): 
    with open(file) as file_in:
        return [line.strip().split(' ') for line in file_in]

print(get_input('input.txt'))
hpos = 0
depth = 0
aim = 0

for command in get_input('input.txt'):
    if command[0] == 'forward':
        hpos += int(command[1])
        depth += aim * int(command[1])
    elif command[0] == 'down':
        aim += int(command[1])
    else: 
        aim -= int(command[1])

print(hpos * depth)
