
import heapq
import sys
"""
1. Varför prducerar algoritmen ett MST?
Kör i princip Dijkstras.
Börjar på en nod och expanderar greedily.
Vår priority-head ger oss snabbt den billigaste kanten
visited gör att vi inte skapar en cykel

2. Tidskomplexitet 
Best Case: O(E*log(V)) - grafen är redan MST
Average: O((V + E) * log(V)) 
    Varje nod besöks exakt en gång och loopar alla 
    sina grannar. 
    heappop körs V gånger -> V*log(V) 
    heappush körs E gånger -> E*log(V)
Worst Case: O(V^2 * log(V))- när E = V. Lång path.  

3. Vad händer när en kant kollapsar?
Kan splittra grafen, och därmed inte nå överallt. 
MST:n gäller inte längre, behöver räkna om. 

4. Verkliga tillämpningar
Olika typer av nätverk.
Kunna reducera nätverk, ta bort dyra kanter. 

5. Krav för att MST ge rätt lösning: 
Alla noder är anslutna, kanterna har kostnad, 
tar inte hänsyn till riktning, flöde eller redundans.

"""

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






