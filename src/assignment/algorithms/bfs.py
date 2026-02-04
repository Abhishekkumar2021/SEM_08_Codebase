from .base import State
from typing import Callable, List, Tuple, Dict
from collections import deque

def construct_path(curr: State, par: Dict) -> List[State]:
    path = []
    
    while curr:
        path.append(curr)
        curr = par[curr]
    
    # reverse
    path = path[::-1]
    
    # Final path
    return path

def bfs(start: State, goal: Callable[[State], bool], successors: Callable[[State], List[State]]) -> Tuple[int, ...]:
    
    q = deque()
    vis = set()
    par = dict()
    
    vis.add(start)
    par[start] = None
    q.append(start)
    
    while q:
        n = len(q)
        while n:
            curr = q.popleft()
            
            if goal(curr):
                return construct_path(curr, par)
            
            for next in successors(curr):
                if next not in vis:
                    vis.add(next)
                    q.append(next)
                    par[next] = curr
                    
            n -= 1
            