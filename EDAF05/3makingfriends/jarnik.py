
import heapq

indata = []

n, m = map(int, input().split())

for i in range(m):
    a, b, w = map(int, input().split())
    indata.append(((a,b), w))

def createGraph(indata: list):
    result= {}
    for (a,b), w in indata:
        if a not in result:
            result[a] = []
        if b not in result:
            result[b] = []
        result[a].append((b,w))
        result[b].append((a,w))
    return result

graph = createGraph(indata)



def jarnik(graph: dict, root: int) -> int :
    T = set()
    T.add(root)
    heap = [(w, root, v) for (v,w) in graph[root]]
    heapq.heapify(heap)

    total = 0

    while heap:
       w, u, v  = heapq.heappop(heap)

       if v in T:
           continue
       
       T.add(v)
       total += w
       for neighbor, weight in graph[v]:
           if neighbor not in T:
               item = (weight, v, neighbor)
               heapq.heappush(heap, item)
    
    return total


def jarnik_new(graph, root, n):
    visited = [False] * (n + 1)
    visited[root] = True

    heap = [(w, v) for (v, w) in graph[root]]
    heapq.heapify(heap)

    total = 0

    heappop = heapq.heappop
    heappush = heapq.heappush
    g = graph

    while heap:
        w, v = heappop(heap)

        if not visited[v]:
            continue

        visited[v] = True
        total += w
 
        for neighbor, weight in g[v]:
            if not visited[neighbor]:
                heappush(heap, (weight, neighbor))

    return total

print(jarnik_new(graph, 1,n))




def prims(graph: dict, start:int):
    Q = set(graph)
    Q.remove(start)

    S = set()   
    S.add(start)

    total = 0

    while Q:
       u, v, w = min(((a, b, w) for a in S for (b,w) in graph[a] if b in Q), key=lambda x: x[2])
       total += w
       Q.remove(v)
       S.add(v)
    return total








