from collections import deque
from help_functions import *
from state import *


#Ändrar tågkartan
def Railway_Planning():

    routes_removed = 0
    capacity = 0
    old_capacity = 0
    i = 1

    for r in remove_route:
        print("Iteration " + str(i))
        (u ,v , c) = edges[r]
        print("u,v,c : " + str((u,v,c)) + "\n")
        print("flow before: " + str(flow) + "\n")
        graph[u][v] = 0
        print("rg before reset: " + str(residual_graph) + "\n")
        fast_reset_rg()
        print("rg after reset: " + str(residual_graph) + "\n")
        reset_flow()
        print("flow after reset: " + str(flow) + "\n")
        capacity = Ford_Fulkerson()
        print("flow after FF: " + str(flow) + "\n")
        if capacity < C_students:
            graph[u][v] = c
        else: 
            routes_removed += 1
            old_capacity = capacity
        i += 1
        print("\n \n")
    
    print(str(routes_removed) + "  " + str(old_capacity))


# Kontrollerar nätverksflöde
def Ford_Fulkerson():
    s = 0
    t = N_nodes - 1
    parent = BFS(residual_graph,s, t)
    delta = float("inf")
    total_flow = []
    path = get_path(parent, s, t)

    while path : 
        print("path: " + str(path) + "\n")
        for p in range(len(path)): 
            u = path[p][0]
            v = path[p][1]
            delta = min(residual_graph[u][v], delta)
            print("delta: " + str(delta) + "\n")
        
        for p in range(len(path)):
            u = path[p][0]
            v = path[p][1]
            update_flow(u,v, delta)

        total_flow.append(delta)
        delta = float("inf")
        print("rg i FF före update: " + str(residual_graph) + "\n")
        Update_Residual_Graph(residual_graph)
        print("rg i  FF efter update: " + str(residual_graph) + "\n")
        parent = BFS(residual_graph,s, t)
        print("parent: " + str(parent) + "\n")
        path = get_path(parent, s, t)
        print("path :" + str(path) + "\n")

    print("total_sum: " + str(total_flow) + "\n")
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




 