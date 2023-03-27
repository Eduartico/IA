import heapq # we'll be using a heap to store the states


def greedy_search(initial_state, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    states = [initial_state]
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