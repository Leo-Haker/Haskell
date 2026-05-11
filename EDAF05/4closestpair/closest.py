import sys
from typing import List
import math

data = sys.stdin.buffer.read().split()

idx = 0

n = int(data[idx]); idx += 1

plane = List
for _ in range(n):
    plane.append((data[idx], data[idx+1]))
    idx += 2



def closest(px: List[tuple], py: List[tuple], n:int ) -> tuple[int, int]:
    (left_px, right_px) = divide(px, n) 
    (left_py, right_py) = divide(py, n)

    minimum = min(subproblem(left_px,left_py), subproblem(right_px, right_py))
    
    

def closest_pair(plane: List[tuple]) : 
    p_x = plane.sort(key=lambda tup: tup[0])
    p_y = plane.sort(key=lambda tup: tup[1])
    closest(p_x, p_y, len(plane))

def divide(size: int, plane: List[tuple]) -> tuple[List[tuple], List[tuple]]:
    return (plane[:size//2], plane[size//2 + 1 :-1])

def distance(p1: tuple[float,float], p2: tuple[float,float]) -> float :
    return math.dist(p1, p2)

def subproblem(px: List[tuple], py: List[tuple]) -> float:
    temp = []
    for p1 in px:
        for p2 in py:
            temp.insert(distance(p1,p2))
    return min(temp)

def subproblem_1(px: List[tuple], py: List[tuple], size:int) -> float:
    delta = float('inf')
    for i in size:
     for j in size:
         d = distance(px[i], py[j])
         if d < delta:
             


