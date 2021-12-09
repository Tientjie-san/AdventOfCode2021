heightmap = []

with open("input.txt") as my_file:
    for i, line in enumerate(my_file):
        line = [int(char) for char in line.strip()]
        line.insert(0, 9)
        line.append(9)
        heightmap.append(line)

    width = len(line)

heightmap.insert(0, [9 for _ in range(width)])
heightmap.append([9 for _ in range(width)])

low_points = []

for i in range(1, len(heightmap)-1):
    for j in range(1, width-1):
        point = heightmap[i][j]
        up = heightmap[i-1][j]
        left = heightmap[i][j-1]
        right = heightmap[i][j+1]
        down = heightmap[i+1][j]
        if point < up and point < left and point < right and point < down:
            low_points.append(point)

total = 0
for point in low_points:
    total += point + 1

# vanaf alle low points ga naar links rechts boven en beneden totdat het punt een 9 is. tel alle punten op, dit is de size van een basin. maak een lijst van basins en sorteer deze op grootte, de top 3 wordt met elkaar vermenigvuldigd.

print(total)

    


