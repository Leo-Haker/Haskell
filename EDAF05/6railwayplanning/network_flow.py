from collections import deque
from help_functions import *
from state import *


#Ändrar tågkartan
def Railway_Planning():

    routes_removed = 0
    capacity = 0
    f = Ford_Fulkerson()
    #print("first f : " + str(f) + "\n")
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

        #print(f"mid={mid}, capacity={capacity}, lower={lower}, higher={higher}")
    reset()
    #print(graph)
    remove_path_binary(lower)
    #print(flow)
    f = Ford_Fulkerson()
    routes_removed = lower
    #print(str(routes_removed) + "  " + str(f))
    #
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
            (u,v,c,f,b,r) = edge_list[edge_idx]
            flow = max(0, c-f)
            print("flow :" + str(flow))
            delta = min(delta, flow)
            print("delta :" + str(delta))
            #print("path : " + str(p) + "\n")
        
        for p in range(len(path)):
            edge_idx = path[p]
            print(delta)
            other_way_idx = edge_list[edge_idx][5]
            print(edge_list[edge_idx][3])
            print(edge_list[other_way_idx][3])
            state.edge_list[edge_idx][3] = edge_list[edge_idx][3] + delta
            state.edge_list[other_way_idx][3] =  edge_list[other_way_idx][3] - delta
            print(edge_list[edge_idx][3])
            print(edge_list[other_way_idx][3])

        total_flow.append(delta)
        delta = float("inf")
        parent = BFS(s, t)
        print(parent)
        path = get_path(parent, s, t)
        print(path)
    

    return sum(total_flow)




# BFS för att se att det går att ta sig från start till slut
def BFS (s,t):
    queue = deque()
    queue.append(s)
    visited = bytearray(N_nodes)
    visited[s] = 1
    parent = [-1] * N_nodes
    #print(parent)

    while queue:
        u = queue.popleft()

        for edge_idx in adj[u]:
            active = edge_list[edge_idx][4]
            #print(adj)
            #print(active)
            if active:
                (eu,v,c,f,b,r) = edge_list[edge_idx]
                cap = c - f

                if not visited[v] and cap > 0:
                    #print(v)
                    #print(edge_idx)
                    visited[v] = 1 
                    queue.append(v)
                    parent[v] = edge_idx
                    if v == t:
                        #print("parent return in while loop: " + str(parent) + "\n")
                        return parent
    #print("parent efter while loop: " + str(parent) + "\n")

    return []




 