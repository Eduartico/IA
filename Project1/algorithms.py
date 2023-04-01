import test_logic as logic
import heapq
import copy


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

            score += (3 - border_distance) * 0.1 + neighbors * 0.2

            # Check for invalid palindromes
            if(not logic.verifyListPalindrome(board[row])): #check if the row is a palindrome
                score += 5
            if(not logic.verifyListPalindrome(logic.transposeBoard(board)[col])): #check if the col is a palindrome
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

import heapq

def a_star(start_state, heuristic, generate_successors):
    visited = []
    queue = [(heuristic(start_state), 0, [start_state])]
    while queue:
        queue.sort(key=lambda x: x[0])
        _, cost, path = queue.pop(0)
        current_state = path[-1]
        if logic.verifyGameEnd(current_state):
            return path, cost
        if current_state in visited:
            continue
        visited.append(current_state)
        for successor_state in generate_successors(current_state):
            if successor_state in visited:
                continue
            successor_cost = 1  # Since each move has a cost of 1
            new_cost = cost + successor_cost
            new_path = path + [successor_state]
            queue.append((new_cost + heuristic(successor_state), new_cost, new_path))
    return None, None




def print5(board):
    dummy = 1
    for i in board:
        if dummy == 5:
            dummy = 1
            print(i)
        else:
            print(i)
            dummy+=1

print5(a_star(logic.boardTest, heuristic, generate_successors))