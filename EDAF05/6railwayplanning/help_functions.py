from state import  *
from copy import copy, deepcopy

def get_capacity(u, v) -> int:
    return original_graph[u][v]

def get_flow(u, v) -> int:
    return flow[u][v]

def update_flow(u,v, c):
    global flow
    flow[u][v] = c

def reset_flow():
    for i in range(N_nodes):
        flow[i][:] = [0] * N_nodes

def fast_reset_rg():
    new = deepcopy(graph)
    for i in range(N_nodes):
        residual_graph[i][:] = new[i][:]

def get_path(parent, s, t):
    if parent == []:
        return []
    
    path = []
    node = t

    while node != s:
        path.append((parent[node], node))
        node = parent[node]
    return path

def Update_Residual_Graph(rg:list[list] ) -> list[list]:
    for u in range(N_nodes):
        for v in range(N_nodes):
            a = get_capacity(u,v)
            b = get_flow(u,v)
            if a > b:
                 rg[u][v]= a - b
                 rg[v][u] = b
            elif a == b:
                rg[u][v] = 0
                rg[v][u] = b
