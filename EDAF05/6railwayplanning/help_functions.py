from state import  *
from copy import copy, deepcopy



def reset():
    for i in range(len(edge_list)):
        edge_list[i][3] = 0
        edge_list[i][4] = True

def get_path(parent, s, t):
    if parent == []:
        return []
    
    path = []
    node = t
    
    while node != s:
        edge_idx = parent[node]
        u = edge_list[edge_idx][0]
        path.append(edge_idx)
        node = u
    return path

def remove_path_binary(mid):
    for r in remove_route[:mid]:
        u = r*2
        v = r*2 +1
        edge_list[u][4] = False
        edge_list[v][4] = False




