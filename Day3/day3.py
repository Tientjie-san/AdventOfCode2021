def get_input(file): 
    with open(file) as file_in:
        return [line.strip() for line in file_in]

puzzle_input = get_input("example.txt")
puzzle_input.sort()
print(puzzle_input)
bovengrens = len(puzzle_input) -1
ondergrens = 0
mid = ondergrens + (bovengrens-ondergrens) // 2


def find_oxy(ondergrens_oxy, bovengrens_oxy):
    for i in range(len(puzzle_input[0])):

        if bovengrens_oxy - ondergrens_oxy == 1:
            return puzzle_input[bovengrens_oxy]
                
        mid_oxy = ondergrens_oxy+ (bovengrens_oxy - ondergrens_oxy) // 2

        if (bovengrens_oxy + 1 - ondergrens_oxy) % 2 == 0:
            if puzzle_input[mid_oxy + 1][i] == '1':
                ondergrens_oxy = mid_oxy 
            else:
                bovengrens_oxy = mid_oxy 
        else:
            if puzzle_input[mid_oxy][i] == '0':
                bovengrens_oxy = mid_oxy
            else: 
                ondergrens_oxy = mid_oxy
        
        
def find_co2(ondergrens_oxy, bovengrens_oxy):
    for i in range(len(puzzle_input[0])):

        if bovengrens_oxy - ondergrens_oxy == 1:
            return puzzle_input[ondergrens]
                

        mid_oxy = ondergrens_oxy+ (bovengrens_oxy - ondergrens_oxy) // 2

        print(f"bovengrens_oxy: {bovengrens_oxy}")
        print(f"ondergrens_oxy: {ondergrens_oxy}")
        print(f"mid_oxy: {mid_oxy}")

        if (bovengrens_oxy + 1 - ondergrens_oxy) % 2 == 0:

            if puzzle_input[mid_oxy + 1][i] == '0':
                ondergrens_oxy = mid_oxy + 1
            else:
                bovengrens_oxy = mid_oxy -1
        else:
            if puzzle_input[mid_oxy][i] == '1':
                bovengrens_oxy = mid_oxy
            else: 
                ondergrens_oxy = mid_oxy


print(find_oxy(ondergrens, bovengrens))
print(find_co2(ondergrens, bovengrens))

