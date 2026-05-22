import sys
from copy import copy, deepcopy

# Läser in input
data = list(map(int, sys.stdin.buffer.read().split()))

idx = 0

N_nodes= data[idx]; idx += 1
M_edges = data[idx]; idx += 1
C_students = data[idx]; idx += 1
P_routes = data[idx]; idx += 1

# Skapar strukturer
graph = [[0] * N_nodes for _ in range(N_nodes)]
original_graph = []
flow = deepcopy(graph)
residual_graph = deepcopy(graph)
edges= []
remove_route = []

for i in range(M_edges):
    u = data[idx]; idx += 1
    v = data[idx]; idx += 1
    c = data[idx]; idx += 1
    graph[u][v] = c
    edges.append((u,v,c))

for i in range(P_routes):
    p = data[idx];idx += 1
    remove_route.append(p)

original_graph = deepcopy(graph)

