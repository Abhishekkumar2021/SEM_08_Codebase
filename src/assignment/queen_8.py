from algorithms.base import print_path, State
from algorithms.bfs import bfs
from typing import List, Tuple

# Initial and Final State
START: State = (0, (-1, -1, -1, -1, -1, -1, -1, -1))

def goal(state: State) -> bool:
    row, _ = state
    return row == 8

def is_safe(board: Tuple, row: int, col: int) -> bool:
    # col check
    for i in range (row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
        
    return True
   
# Successors function
def successors(state: State) -> List[State]:
    row, board = state

    next_states = []
    
    for col in range(8):
        # Check safety
        if not is_safe(board, row, col):
            continue
        
        # Converting to mutable list
        copy: List = list(board)[::]
        
        # Updation
        copy[row] = col
        
        # converting back to mutable state
        next_states.append((row + 1, tuple(copy)))
        
    return next_states   

path = bfs(START, goal, successors)

print_path(path)