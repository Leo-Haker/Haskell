import sys
from typing import List
import math
import time

data = sys.stdin.buffer.read().split()

idx = 0

n = int(data[idx]); idx += 1

theplane = []
f = float
theplane = [(f(data[i]), f(data[i+1]))
            for i in range(idx, idx + 2*n, 2)]

def closest_pair(plane: List[tuple]) -> float: 
    p_x = sorted(plane, key=lambda t: t[0])
    p_y = sorted(plane, key=lambda t: t[1])
    return closest(p_x, p_y, len(plane))

def closest(px: List[tuple], py: List[tuple], n:int ) -> float:
    if n <= 3:
        return brute(px)



    (left_px, right_px) = divide(px, n) 

    #viktigt checka om ett element finns i ett sett är O(1) innan hade jag O(n) så tog väldigt långt tid att bygga left/right_py
    left_set = set(left_px)

    (left_py, right_py) = ([],[])

    finns = left_set.__contains__

    for p in py:
        if finns(p):
            left_py.append(p)
        else:
            right_py.append(p)

    delta_left = closest(left_px, left_py, len(left_px))
    delta_right = closest(right_px, right_py, len(right_px))

    delta = min(delta_left, delta_right)

    mid_x = px[n//2][0]

    ps = list(filter(lambda p1: abs(p1[0] - mid_x) < delta, py))
    
    return min(delta, strip(ps, delta))

def strip(ps: List[tuple], delta: float) -> float:
    res = float('inf')
    #ändrade från i+8 till i+3 som funkade men i+2 funkade inte gick snabbare också
    for i in range(len(ps)):
        for j in range(i+1, min(i+3, len(ps))):
            res = min(distance(ps[i], ps[j]), res)
    return res

def brute(p: List[tuple]) -> float:
    s = float('inf')
    size = len(p)
    for i in range(size):
        for j in range(size):
            if i > j:
                temps = distance(p[i], p[j])
                if temps < s:
                    s = temps
    return s

def divide(plane: List[tuple], size: int) -> tuple[List[tuple], List[tuple]]:
    return ((plane[:size//2], plane[size//2:]))

def distance(p1: tuple[float,float], p2: tuple[float,float]) -> float :
    return math.dist(p1, p2)


def main():
    start = time.perf_counter()

    result = closest_pair(theplane)

    #result = brute(theplane)

    end = time.perf_counter()

    print(f"{result:.6f}")
    print(f"Time: {(end - start)*1000:.3f} ms", file=sys.stderr)    #.6f means fixed-point float exakt 6 digits va


if __name__ == "__main__":
    main()