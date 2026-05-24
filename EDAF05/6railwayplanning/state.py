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
remove_route = []
edge_list = [] #[(u, v, c, flow, activated, inverse edge index)]
adj = [[] for _ in range(N_nodes)]
##print("id för edge_list i state : " + str(id(edge_list)))

def add_edge(u, v, c):
    fwd = len(edge_list)
    bwd = fwd + 1
    adj[u].append(len(edge_list))
    edge_list.append([u, v, c, 0, True, bwd])
    adj[v].append(len(edge_list))
    edge_list.append([v, u, c, 0, True, fwd])
    ##print("id för edge_list i vid tilldelning : " + str(id(edge_list)))
    

for i in range(M_edges):
    u = data[idx]; idx += 1
    v = data[idx]; idx += 1
    c = data[idx]; idx += 1
    add_edge(u, v, c)

for i in range(P_routes):
    p = data[idx];idx += 1
    remove_route.append(p)


