import sys


data = list(map(int, sys.stdin.buffer.read().split()))

idx = 0

N_nodes= data[idx]; idx += 1
M_edges = data[idx]; idx += 1
C_students = data[idx]; idx += 1
P_routes = data[idx]; idx += 1

# capacaty of network >= C_students

graph = {} 
remove_route = []

for i in range(M_edges):
    p = (u,v,c) = data[idx], data[idx+1], data[idx+1]
    graph[i] = p
    idx += 3

for i in range(P_routes):
    p = data[idx];idx += 1
    remove_route.append(p)