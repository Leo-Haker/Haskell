from state import  *
from copy import copy, deepcopy



def reset():
    for i in range(len(adj)):
        edge_idx = adj[i]
        (u, v, c, f, b, r) = edge_list[edge_idx]
        add_edge(u,v,c)


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

def remove_path_binary(mid):
    for r in remove_route[:mid]:
        (u, v, c, f, b, r) = edge_list[r]
        edge_list[u][4] = False
        edge_list[v][4] = False




