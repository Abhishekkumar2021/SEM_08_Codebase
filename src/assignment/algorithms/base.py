from typing import List

# State type
type State = int

def print_path(path: List[State])-> None:
    n = len(path)
    for i in range(n):
        if i == n - 1:
            print(path[i])
        else:
            print(path[i], end=' --> ') 
