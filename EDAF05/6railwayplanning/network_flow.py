from collections import deque
import sys


data = list(map(int, sys.stdin.buffer.read().split()))

idx = 0

N_nodes= data[idx]; idx += 1
M_edges = data[idx]; idx += 1
C_students = data[idx]; idx += 1
P_routes = data[idx]; idx += 1

# capacaty of network >= C_students

graph = [[0] * N_nodes for _ in range(N_nodes)]
flow = [[0] * N_nodes for _ in range(N_nodes)]
remove_route = []


for i in range(M_edges):
    u = data[idx]; idx += 1
    v = data[idx]; idx += 1
    c = data[idx]; idx += 1
    graph[u][v] = c

for i in range(P_routes):
    p = data[idx];idx += 1
    remove_route.append(p)


## enkel schematisk grund
def BFS (G:list[list] ,s,t, parent:list):
    queue = deque()
    queue.append(s)
    visited = bytearray(N_nodes)
    visited[s] = 1

    while queue:
        u = queue.popleft()

        for v in range(len(G)):
            if not visited[v] and G[u][v] > 0:
                visited[v] = 1 
                queue.append(v)
                parent[v] = u
                if v == t:
                    return True
    return False

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
                
def Ford_Fulkerson():
    graph:list[list]
    rg = graph.copy()
    rg:list[list]
    flow:list[list]
    while BFS: 
        "do stuff"
    return