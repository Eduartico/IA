import test_logic as logic
import heapq
import copy
from collections import Counter

def compare_halfs(board):
    score = 0
    n = len(board)

    for row in range(n):
        half = n // 2
        left_half = [board[row][col] for col in range(half) if board[row][col] != ' ']
        right_half = [board[row][col] for col in range(half, n) if board[row][col] != ' ']

        # Count the number of pieces of each color in the left and right halves of the row
        left_counts = Counter(left_half) # ex: returns {'R': 2, 'G': 1}
        right_counts = Counter(right_half)

        # Compare the counts and update the score accordingly
        for color in ['R', 'G', 'B']:
            count_diff = abs(left_counts[color] - right_counts[color]) 
            score += count_diff

    return score


def heuristic_compare_halfs(board):
    score_rows = compare_halfs(board)
    board_transposed = logic.transposeBoard(board)
    score_cols = compare_halfs(board_transposed)
    return score_rows + score_cols

def heuristic(board):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            # Get piece type
            piece = board[row][col]

            # Calculate distance from the border
            border_distance = min(row, col, len(board) - row - 1, len(board[0]) - col - 1)

            # Calculate number of neighbors of the same type on the same row and column
            row_neighbors = sum(1 for c in range(len(board[0])) if board[row][c] != ' ' and c != col)
            col_neighbors = sum(1 for r in range(len(board)) if board[r][col] != ' ' and r != row)
            neighbors = row_neighbors + col_neighbors

            score += (len(board) - border_distance) * 0.1 + neighbors * 0.2

            # Check for invalid palindromes
            if(not logic.verifyListPalindrome(logic.transposeBoard(board)[col])): #check if the col is a palindrome
                score += 5
        if(not logic.verifyListPalindrome(board[row])): #check if the row is a palindrome
            score += 5
    return score

# Define a function to generate all possible successors
def generate_successors(board):
    successors = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            # Skip non empty cells
            if not board[r][c] == ' ':
                continue
            # Check horizontal moves
            new_board = copy.deepcopy(board)
            new_board[r][c] = 'R'
            successors.append(new_board)
            new_board2 = copy.deepcopy(board)
            new_board2[r][c] = 'G'
            successors.append(new_board2)
            new_board3 = copy.deepcopy(board)
            new_board3[r][c] = 'B'
            successors.append(new_board3)
    return successors



def a_star(start_state, heuristic, generate_successors):
    visited = []
    queue = [(heuristic(start_state), start_state)]
    while queue:
        successors = []
        queue.sort(key=lambda x: x[0])
        _, current_state = queue.pop(0)
        if logic.verifyGameEnd(current_state):
            return current_state
        if current_state in visited:
            continue
        visited.append(current_state)
# Generate successors and add to queue
        successors = generate_successors(current_state)
        if successors:
            for successor in successors:
                # Check if successor has already been visited
                if successor not in visited:
                    queue.append((heuristic(successor), successor))
    return "No results found :("

def print5(board):
    dummy = 1
    if board:
        for i in board:
            if dummy == 5:
                dummy = 1
                print(i)
            else:
                print(i,)
                dummy+=1

#print5(generate_successors(logic.boardTest))

print5(a_star(logic.boardTest, heuristic, generate_successors))