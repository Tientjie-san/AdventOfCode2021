fish_counts = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0
}

with open('input.txt') as my_file:
    for line in my_file:
        line = line.strip().split(",")
        for num in line:
            fish_counts[num] += 1
    

days = 256

for day in range(days):
    new_zero = fish_counts["1"]
    new_one = fish_counts["2"]
    new_seconds = fish_counts["3"]
    new_thirds = fish_counts["4"]
    new_fourths = fish_counts["5"]
    new_fifths = fish_counts["6"]
    new_six = fish_counts["7"] + fish_counts["0"]
    new_seven = fish_counts["8"]
    new_8 = fish_counts["0"]

    fish_counts["0"] = new_zero
    fish_counts["1"] = new_one
    fish_counts["2"] = new_seconds
    fish_counts["3"] = new_thirds
    fish_counts["4"] = new_fourths
    fish_counts["5"] = new_fifths
    fish_counts["6"] = new_six
    fish_counts["7"] = new_seven
    fish_counts["8"] = new_8

total = 0
for amount in fish_counts.values():
    total += amount

print(total)