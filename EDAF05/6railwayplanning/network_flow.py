from collections import deque
from help_functions import *
from state import *


#Ändrar tågkartan
def Railway_Planning():

    routes_removed = 0
    capacity = 0
    f = Ford_Fulkerson()
    lower = 0
    higher = len(remove_route)

    while lower < higher:
        reset()
        mid = (lower + higher + 1)//2
        remove_path_binary(mid)
        capacity = Ford_Fulkerson()
        if capacity >= C_students:
            lower = mid
            f = capacity
        else:
            higher = mid -1
            f = capacity


    reset()
    remove_path_binary(lower)
    f = Ford_Fulkerson()
    routes_removed = lower
    print(str(routes_removed) + "  " + str(f))

# Om svaret på problemet är x, så betyder det att man får flow >= C när man tar bort de x första kanterna, 
# men flow < C när man tar bort de x+1 första kanterna (Optimering?)


# Kontrollerar nätverksflöde
def Ford_Fulkerson():
    global edge_list
    s = 0
    t = N_nodes - 1
    parent = BFS(s, t)
    delta = float("inf")
    total_flow = []
    path = get_path(parent, s, t)

    while path: 
        for p in range(len(path)): 
            edge_idx = path[p]
            c = edge_list[edge_idx][2]
            f = edge_list[edge_idx][3]
            flow = max(0, c-f)
            delta = min(delta, flow)
        
        for p in range(len(path)):
            edge_idx = path[p]
            other_way_idx = edge_list[edge_idx][5]
            edge_list[edge_idx][3] += delta
            edge_list[other_way_idx][3] -= delta

        total_flow.append(delta)
        delta = float("inf")
        parent = BFS(s, t)
        path = get_path(parent, s, t)
    
    return sum(total_flow)




# BFS för att se att det går att ta sig från start till slut
def BFS (s,t):
    queue = deque()
    queue.append(s)
    visited = bytearray(N_nodes)
    visited[s] = 1
    parent = [-1] * N_nodes

    while queue:
        u = queue.popleft()

        for edge_idx in adj[u]:
            active = edge_list[edge_idx][4]
            if active:
                v = edge_list[edge_idx][1]
                c = edge_list[edge_idx][2]
                f = edge_list[edge_idx][3]
                cap = c - f

                if not visited[v] and cap > 0:
                    visited[v] = 1 
                    queue.append(v)
                    parent[v] = edge_idx
                    if v == t:
                        return parent
    return []




 