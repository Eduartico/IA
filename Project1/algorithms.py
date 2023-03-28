import test_logic as logic
import heapq


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
            # Skip empty cells
            if board[r][c] == ' ':
                continue
            # Check horizontal moves
            for nc in range(len(board[0])):
                if nc == c:
                    continue
                if board[r][nc] == ' ':
                    new_board = [row[:] for row in board]
                    new_board[r][c], new_board[r][nc] = new_board[r][nc], new_board[r][c]
                    successors.append((new_board, (r, c), (r, nc)))
            # Check vertical moves
            for nr in range(len(board)):
                if nr == r:
                    continue
                if board[nr][c] == ' ':
                    new_board = [row[:] for row in board]
                    new_board[r][c], new_board[nr][c] = new_board[nr][c], new_board[r][c]
                    successors.append((new_board, (r, c), (nr, c)))
    return successors

# Define the A* search function
def astar(start_board, goal_board, heuristic):
    # Define a helper function to calculate the cost of a path
    def cost(path):
        return sum(heuristic(board, *pos) for board, pos in path)

    # Initialize the search
    start_pos = [(r, c) for r in range(len(start_board)) for c in range(len(start_board[0])) if start_board[r][c] != ' ']
    start_state = (start_board, tuple(start_pos))
    goal_pos = [(r, c) for r in range(len(goal_board)) for c in range(len(goal_board[0])) if goal_board[r][c] != ' ']
    goal_state = (goal_board, tuple(goal_pos))
    closed = set()
    fringe = [(cost([start_state]), [start_state])]

    # Search until the fringe is empty or a goal state is found
    while fringe:
        # Get the next state from the fringe
        _, path = heapq.heappop(fringe)
        state = path[-1]
        if state == goal_state:
            return path
        if state in closed:
            continue
        closed.add(state)

        # Generate successors and add them to the fringe
        for new_board, pos1, pos2 in generate_successors(state[0]):
            new_pos = list(state[1])
            new_pos[new_pos.index(pos1)] = pos2
            new_state = (new_board, tuple(new_pos))
            new_path = path + [new_state]
            heapq.heappush(fringe, (cost(new_path), new_path))

    # No path found
    return None


