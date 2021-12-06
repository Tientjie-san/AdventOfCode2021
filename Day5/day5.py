covered_positions = dict()

with open('input.txt') as my_file:
    for line in my_file:
        line = line.strip()
        segments = line.split (" -> ")
        start = segments[0].split(",")
        end = segments[-1]. split(",")
        start = [int(point) for point in start]
        end = [int(point) for point in end]

        # horizontal
        if start[0] == end[0]:
            if end[1] > start[1]:
                for i in range(start[1], end[1] + 1):
                    covered_positions[str([start[0],i])] = covered_positions.get(str([start[0],i]), 0) + 1
            else:
                for i in range(end[1], start[1] + 1):
                    covered_positions[str([start[0],i])] = covered_positions.get(str([start[0],i]), 0) + 1
        # vertical
        elif start[1] == end[1]:
            if end[0] > start[0]:
                for i in range(start[0], end[0] + 1):
                    covered_positions[str([i,start[1]])] = covered_positions.get(str([i, start[1]]), 0) + 1
            else:
                for i in range(end[0], start[0] + 1):
                    covered_positions[str([i,start[1]])] = covered_positions.get(str([i, start[1]]), 0) + 1 
        # diagonal
        elif start[1] > end[1]:
            # omlaag
            for i in range(0, start[1]- end[1] + 1):
                # naar rechts
                if start[0] < end[0]:
                    covered_positions[str([start[0]+ i ,start[1] - i])] = covered_positions.get(str([start[0] + i, start[1] -i]), 0) + 1
                else: 
                    covered_positions[str([start[0]- i ,start[1] - i])] = covered_positions.get(str([start[0]- i, start[1] -i]), 0) + 1
        else:
            #omhoog
            for i in range(0, end[1]- start[1] + 1):
                # naar rechts
                if start[0] < end[0]:        
                    covered_positions[str([start[0]+ i ,start[1]+ i])] = covered_positions.get(str([start[0] + i, start[1] +i]), 0) + 1
                else: 
                    covered_positions[str([start[0]- i ,start[1]+ i])] = covered_positions.get(str([start[0] - i, start[1] +i]), 0) + 1

                    
count = 0
for value in covered_positions.values():
    if value >= 2:
        count += 1
print(count)