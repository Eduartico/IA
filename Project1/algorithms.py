import test_logic as logic
import heapq
import copy


def heuristic(board, row, col):
    # Get piece type
    piece = board[row][col]

    # Calculate distance from the border
    border_distance = min(row, col, len(board) - row - 1, len(board[0]) - col - 1)

 # Calculate number of neighbors of the same type on the same row and column
    row_neighbors = sum(1 for c in range(len(board[0])) if board[row][c] != ' ' and c != col)
    col_neighbors = sum(1 for r in range(len(board)) if board[r][col] != ' ' and r != row)
    neighbors = row_neighbors + col_neighbors

    score = 0
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

def astar_search(start_state, heuristic_func, successor_func):
    """Performs A* search to find a solution from start_state."""
    # Initialize start node
    start_node = (heuristic_func(start_state), start_state)
    # Initialize priority queue with start node
    frontier = [start_node]
    # Initialize set of visited states
    visited = set()
    # Initialize dictionary to keep track of parent nodes
    parent_dict = {start_state: None}
    # Initialize dictionary to keep track of g scores
    g_dict = {start_state: 0}

    # Continue searching until the frontier is empty
    while frontier:
        # Get the node with the lowest f score from the frontier
        current_node = heapq.heappop(frontier)
        current_state = current_node[1]

        # Check if current state is the goal state
        if logic.verifyGameEnd(current_state):
            # If it is, return the path to the goal state
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent_dict[current_state]
            path.reverse()
            return path

        # Mark current state as visited
        visited.add(current_state)

        # Generate successor states and add them to the frontier
        for successor_state in successor_func(current_state):
            # Calculate the g score for the successor state
            g_score = g_dict[current_state] + 1

            # Check if successor state has been visited or is in the frontier
            if successor_state in visited:
                continue
            for f, state in frontier:
                if state == successor_state:
                    if g_score >= g_dict[successor_state]:
                        continue
                    else:
                        frontier.remove((f, state))
                        heapq.heapify(frontier)
                    break

            # Update the parent and g score dictionaries
            parent_dict[successor_state] = current_state
            g_dict[successor_state] = g_score

            # Calculate the f score for the successor state and add it to the frontier
            f_score = g_score + heuristic_func(successor_state)
            heapq.heappush(frontier, (f_score, successor_state))

    # If the frontier is empty and no solution has been found, return None
    return None

print(astar_search(logic.boardWin, heuristic, generate_successors))