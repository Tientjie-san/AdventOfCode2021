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
print(most_common[0][1] - most_common[-1][1])
    
        
