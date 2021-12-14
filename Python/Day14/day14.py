"""Part 1"""

from collections import Counter

polymer_template = dict()
with open("example.txt") as my_file:
    for i, line in enumerate(my_file):
        if i == 0:
            start_string = line.strip()
        elif i > 1:
            line = line.strip().split(" -> ")
            polymer_template[line[0]] = line[1]

for _ in range(10):
    characters_to_be_inserted = [polymer_template[start_string[i] + start_string[i+1]] for i in range(len(start_string)-1)]
    positions = -2 
    
    
    for i in range(len(characters_to_be_inserted)):
        position = -1 + 2 * (i+1)
        start_string=start_string[:position] + characters_to_be_inserted[i] + start_string[position:]
    
c = Counter(start_string)
most_common = c.most_common()
print(c)

print(most_common[0][1] - most_common[-1][1])
    
        
"""Part 2"""

from collections import defaultdict

count_pairs = dict()

polymer_template = dict()
with open("input.txt") as my_file:
    for i, line in enumerate(my_file):
        if i == 0:
            start_string = line.strip()
        elif i > 1:
            line = line.strip().split(" -> ")
            polymer_template[line[0]] = line[1]
            count_pairs[line[0]] = 0

pairs = [start_string[i] + start_string[i+1] for i in range(len(start_string)-1)]
for pair in pairs:
    count_pairs[pair] += 1

for _ in range(40):
    new_dict = defaultdict(int)
    for pair, count in count_pairs.items():
        new_char = polymer_template[pair]
        new_pairs = (pair[0]+new_char, new_char + pair[1])
        for pair in new_pairs:
            new_dict[pair] += count

    count_pairs = new_dict

char_counter = defaultdict(int)

for pair, count in count_pairs.items():
    for char in pair:
        char_counter[char] += count

for char, count in char_counter.items():
    if count % 2 == 0:
        char_counter[char] = count/2
    else:
        char_counter[char] = count //2 +1

sorted_count = sorted(char_counter.values(), reverse=True)
print(int(sorted_count[0] -  sorted_count[-1]))
