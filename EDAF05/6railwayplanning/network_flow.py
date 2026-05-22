from collections import deque
from help_functions import *
from state import *


#Ändrar tågkartan
def Railway_Planning():

    routes_removed = 0
    capacity = 0
    fast_reset_rg()
    f = Ford_Fulkerson()
    lower = 0
    higher = len(remove_route)

    while lower < higher:
        reset_graph()
        mid = (lower + higher + 1)//2
        remove_path_binary(mid)
        fast_reset_rg()
        reset_flow()
        capacity = Ford_Fulkerson()
        
        if capacity >= C_students:
            lower = mid
            f = capacity
        else:
            higher = mid -1
            f = capacity

        #print(f"mid={mid}, capacity={capacity}, lower={lower}, higher={higher}")
    reset_graph()
    #print(graph)
    remove_path_binary(lower)
    #print(graph)
    fast_reset_rg()
    #print(residual_graph)
    reset_flow()
    #print(flow)
    f = Ford_Fulkerson()
    routes_removed = lower
    print(str(routes_removed) + "  " + str(f))
    #
# Om svaret på problemet är x, så betyder det att man får flow >= C när man tar bort de x första kanterna, 
# men flow < C när man tar bort de x+1 första kanterna (Optimering?)
""" for r in remove_route:
        (u ,v , c) = edges[r]
        graph[u][v] = 0
        graph[v][u] = 0
        fast_reset_rg()
        reset_flow()
        capacity = Ford_Fulkerson()
        if capacity < C_students:
            graph[u][v] = c
            graph[v][u] = c
            break
        else: 
            routes_removed += 1
            f = capacity
    
    print(str(routes_removed) + "  " + str(f))
"""



# Kontrollerar nätverksflöde
def Ford_Fulkerson():
    s = 0
    t = N_nodes - 1
    parent = BFS(residual_graph,s, t)
    delta = float("inf")
    total_flow = []
    path = get_path(parent, s, t)

    while path and i < 4000: 
        for p in range(len(path)): 
            u = path[p][0]
            v = path[p][1]
            delta = min(residual_graph[u][v], delta)
        
        for p in range(len(path)):
            u = path[p][0]
            v = path[p][1]
            update_flow(u,v, delta)

        total_flow.append(delta)
        delta = float("inf")
        Update_Residual_Graph(residual_graph)
        parent = BFS(residual_graph,s, t)
        path = get_path(parent, s, t)

    return sum(total_flow)




# BFS för att se att det går att ta sig från start till slut
def BFS (g:list[list] ,s,t):
    queue = deque()
    queue.append(s)
    visited = bytearray(N_nodes)
    visited[s] = 1
    parent = [-1] * N_nodes

    while queue:
        u = queue.popleft()

        for v in range(len(g)):
            if not visited[v] and g[u][v] > 0:
                visited[v] = 1 
                queue.append(v)
                parent[v] = u
                if v == t:
                    return parent
    return []




 