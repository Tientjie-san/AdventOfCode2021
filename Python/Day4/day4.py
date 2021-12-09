numbers = None
boards = []
board = []

example = "example.txt"
input = "input.txt"

with open("input.txt") as file_in:
    for line in file_in:
        line = line.strip()
        if numbers is None:
            numbers = line.split(',')
        elif line:
            board.append(line.split())
        else:
            if board:
                boards.append(board)
                board = []

boards.append(board)


def sum_unmarked(numbers_seen, board):
    total = 0
    for line in board:
        for number in line:
            if number not in numbers_seen:
                total += int(number)

    return total

def is_bingo(numbers_seen, board):
    for i in range(5):
        row = board[i]
        col = []
        for j in range(5):
            col.append(board[j][i])


        if all(number in numbers_seen for number in row):
            return True
            
        if all(number in numbers_seen for number in col):
            return True
    return False
        


def get_score(numbers, boards):
    
    numbers_seen = []

    for number in numbers:
        if len(boards) == 0:
            break
        numbers_seen.append(number)
        


        for board in boards:
            if is_bingo(numbers_seen, board):
                boards.remove(board)
                last_number = number
                last_board = board

    total_unmarked = sum_unmarked(numbers_seen, last_board)
    score = int(last_number) * total_unmarked
    return score

print(get_score(numbers, boards))



