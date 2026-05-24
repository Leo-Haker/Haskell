from state import  *
from copy import copy, deepcopy

def get_capacity(u, v) -> int:
    return graph[u][v]

def get_flow(u, v) -> int:
    return flow[u][v]

def update_flow(u,v, delta):
    global flow
    flow[u][v] += delta
    flow[v][u] -= delta

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
        edge_idx = parent[node]
        (u, v, c, f, b, r) = edge_list[edge_idx]
        path.append(edge_idx)
        node = u
    return path

def Update_Residual_Graph(rg:list[list] ) -> list[list]:
    for u in range(N_nodes):
        for v in range(N_nodes):
            
            a = get_capacity(u,v)
            b = get_flow(u,v)
            if a == 0 and b == 0:
                continue
            rg[u][v] = max(0, a-b)

def remove_path_binary(mid):
    for r in remove_route[:mid]:
        (u,v,c) = edges[r]
        graph[u][v] = 0
        graph[v][u] = 0

def reset_graph():
    new = deepcopy(original_graph)
    for i in range(N_nodes):
        graph[i][:] = new[i][:]




