from collections import deque
from copy import copy, deepcopy
import sys


data = list(map(int, sys.stdin.buffer.read().split()))

idx = 0

N_nodes= data[idx]; idx += 1
M_edges = data[idx]; idx += 1
C_students = data[idx]; idx += 1
P_routes = data[idx]; idx += 1

# capacaty of network >= C_students

graph = [[0] * N_nodes for _ in range(N_nodes)]
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


## enkel schematisk grund
def BFS (g:list[list] ,s,t):
    queue = deque()
    queue.append(s)
    visited = bytearray(N_nodes)
    visited[s] = 1
    parent = [-1] * N_nodes

    while queue:
        u = queue.popleft()

        for v in range(len(g)):
            if not visited[v] and get_flow(u,v) < g[u][v]:
                visited[v] = 1 
                queue.append(v)
                parent[v] = u
                if v == t:
                    return parent
    return []

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

def get_capacity(u, v) -> int:
    return graph[u][v]

def get_flow(u, v) -> int:
    return flow[u][v]

def update_flow(u,v, c):
    flow[u][v] = c

def reset_flow():
    global flow 
    flow = [[0] * N_nodes for _ in range(N_nodes)]

def fast_reset_rg():
    global residual_graph
    residual_graph = deepcopy(graph)

def get_path(parent, s, t):
    if parent == []:
        return []
    
    path = []
    node = t

    while node != s:
        path.append((parent[node], node))
        node = parent[node]
    return path

                
def Ford_Fulkerson():
    s = 0
    t = N_nodes - 1
    parent = BFS(residual_graph,s, t)
    delta = float("inf")
    total_flow = []
    path = get_path(parent, s, t)
    
    while path : 
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

def Railway_Planning():
    routes_removed = 0
    capacity = 0

    for r in remove_route:
        (u ,v , c) = edges[r]
        graph[u][v] = 0
        reset_flow()
        fast_reset_rg()
        old_capacity = capacity
        capacity = Ford_Fulkerson()
        if capacity < C_students:
            graph[u][v] = c
        else: 
            routes_removed += 1
            old_capacity = capacity
    
    print(str(routes_removed) + "  " + str(capacity))

def main():
    Railway_Planning()

main()