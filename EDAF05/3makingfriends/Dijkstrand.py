def djikstrand(graph: dict, start:int):
    d ={start:0}
    pred = {start:start}
    Q = set(graph)
    Q.remove(start)
    total = 0

    S = set()   
    S.add(start)

    while Q:
       u, v, dist = min(((a, b, d[a] + w) for a in S for (b,w) in graph[a] if b in Q), key=lambda x: x[2])
       d[v] = dist
       pred[v] = u

       Q.remove(v)
       S.add(v)
    return d