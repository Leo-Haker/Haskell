

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

Q = set(graph)
print((n,m))
print(graph)
print(graph[1])
print(Q)

def djikstrand(graph: list, start:int):
    d ={start:0}
    pred = {start:start}
    Q = set(graph)
    Q.remove(start)

    S = set()   
    S.add(start)

    while Q:
       u, v, dist = min(((a, b, d[a] + w) for a in S for (b,w) in graph[a] if b in Q), key=lambda x: x[2])
       d[v] = dist
       pred[v] = u
       Q.remove(v)
       S.add(v)
    return d

print (djikstrand(graph, 1))




