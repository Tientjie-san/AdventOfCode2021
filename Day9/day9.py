from collections import deque

"""
PART 1
"""

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


print(total)



"""
Part 2
"""

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
            # store position of the low point
            low_points.append((j, i))

# to get size of a basin we use BFS algortithm. If value is 9 we dont add it to the queue

basins = []

for point in low_points:
    seen = set(point)
    queue = deque([point])
    count = 0
    while queue:

        point = queue.pop()

        # add neighbours if not 9
        up = (point[0], point[1]+1)
        down = (point[0], point[1]-1)
        left = (point[0]-1, point[1])
        right = (point[0]+1, point[1])
        
        neighbours = [up, down, left, right]

        for neighbour in neighbours:
            if neighbour not in seen:
                seen.add(neighbour)
                if heightmap[neighbour[1]][neighbour[0]] != 9:
                    queue.append(neighbour)
                    count += 1

    
    basins.append(count)


sorted_basins = sorted(basins, reverse=True)
print(sorted_basins[0]*sorted_basins[1]*sorted_basins[2])






# def move_up(x, y):

#     count = 0

#     for i in range(y-1, 0, -1):
#         up = heightmap[i][x]
#         if up != 9:
#             count += 1
#         else:
#             return count
#     return count

# def move_down(x, y):

#     count = 0
#     for i in range(y + 1, len(heightmap)):
#         down = heightmap[i][x]
#         if down != 9:
#             count += 1
#         else:
#             return count
#     return count

# def move_left(x, y):
#     count = 0
#     for i in range(x-1, 0,-1):
#         left= heightmap[y][i]
#         if left != 9:
#             count += 1
#             count += move_up(i, y)
#             count += move_down(i, y)
#         else:
#             return count
#     return count


# def move_right(x, y):
#     count = 0
#     for i in range(x+1, width):
#         right= heightmap[y][i]
#         if right != 9:
#             count += 1
#             count += move_up(i, y)
#             count += move_down(i, y)
#         else:
#             return count

#     return count


    
# basins = []

# for point in low_points:
#     basins_size = 1
#     horizontal_points = []

#     # move up
#     basins_size += move_up(point[0], point[1])
    
#     # move down
#     basins_size += move_down(point[0], point[1])

#     # move left

#     basins_size += move_left(point[0], point[1])

#     # move right

#     basins_size += move_right(point[0], point[1])

#     print(basins_size)
#     basins.append(basins_size)

# print(basins)
# sorted_basins = sorted(basins, reverse=True)
# print(sorted_basins)
# print(sorted_basins[0] * sorted_basins[1] * sorted_basins[2])
