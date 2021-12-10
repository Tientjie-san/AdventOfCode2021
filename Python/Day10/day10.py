from collections import deque

with open("input.txt") as my_file:
    puzzle_input = [line.strip() for line in my_file]


open = ['(', '[', '<', '{']
score_dict = {
        '(': 1, 
        '[': 2, 
        '{': 3, 
        '<': 4
    }

count = 0
scores = []
for line in puzzle_input:
    queue = deque([])
    score = 0
    corrupted = False
    
    for char in  line:
        if char in ['(', '[', '{', '<']:
            queue.append(char)
        elif char == ')':
            if queue[-1] != '(':
                count += 3
                corrupted = True
                break
            else:
                queue.pop()
        elif char == ']':
            if queue[-1] != '[':
                count += 57
                corrupted = True
                break
            else:
                queue.pop()
        elif char == '}':
            if queue[-1] != '{':
                count += 1197
                corrupted = True
                break
            else:
                queue.pop()
        elif char == '>':
            if queue[-1] != '<':
                count += 25137
                corrupted = True
                break
            else:
                queue.pop()
    if not corrupted:
        for char in reversed(queue):
            score = score * 5 + score_dict[char]
        scores.append(score)

print(sorted(scores)[len(scores)//2])        
