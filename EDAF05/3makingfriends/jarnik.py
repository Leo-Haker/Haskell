
import heapq
import sys

data = sys.stdin.buffer.read().split()
idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a = int(data[idx]); idx += 1
    b = int(data[idx]); idx += 1
    w = int(data[idx]); idx += 1
    graph[a].append((b, w))
    graph[b].append((a, w))


def jarnik(graph, root, n):
    visited = bytearray(n + 1) # snabbare än lista med bools
    visited[root] = 1

    heap = [(w, v) for (v, w) in graph[root]]
    heapq.heapify(heap)

    total = 0

    heappop = heapq.heappop
    heappush = heapq.heappush
    g = graph

    while heap:
        w, v = heappop(heap)

        if not visited[v]:

            visited[v] = 1
            total += w
 
            for neighbor, weight in g[v]:
                if not visited[neighbor]:
                    heappush(heap, (weight, neighbor))

    return total



sys.stdout.write(str(jarnik(graph, 1, n)) + '\n') #snabbare än print()






