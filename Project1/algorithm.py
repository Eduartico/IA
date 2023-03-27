import heapq # we'll be using a heap to store the states



boardAlmostWin = [
    [' ', ' ', ' ', 'B', 'R'],
    ['R', 'B', 'B', 'R', ' '],
    ['G', 'G', 'G', ' ', 'G'],
    ['G', 'B', 'B', 'B', 'G'],
    ['R', ' ', 'R', ' ', 'R']
]

def getListOfMoves(board):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ' ':
                moves.append([row, col])
    return moves


def greedy_search(initial_board, heuristic):
    # initial_board (SymmetryPuzzle) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer saying how many rows and columns are left to complete
    states = [initial_board]
    visited = set() 

    setattr(SymmetryPuzzle, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    
    while states:
        current_state = heapq.heappop(states)

        if current_state.is_complete():
            return current_state.move_history

        visited.add(current_state)

        for child_state in current_state.children():
            if child_state not in visited:
                heapq.heappush(states, child_state)
        
    return None



def uniform_cost(initial_board):
    # initial_board(SymmetryPuzzle) - the initial state
    queue = [initial_board]
    visited = set() # to not visit the same state twice
    
    while queue:
        board = queue.pop(0)
        if board in visited:
            continue
        else:
            visited.add(board)

        if board.is_complete():   # check goal state
            return board.move_history
        
        # make moves
        moves = board.children()
        for move in moves:
            queue.append(move)
    return None
