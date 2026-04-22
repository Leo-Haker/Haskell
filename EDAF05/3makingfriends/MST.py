pairs = []

n, m = map(int, input().split())

for _ in range(m):
    a, b, w = map(int, input().split())
    pairs.append(((a, b), w))


print(pairs)
def mst(pairs: list[tuple[tuple[int, int], int]], start: int) ->  int:
    tot_min = 0
    locked_in = []
    current_nodes = []
    current_nodes.insert(pairs.pop())
    for (a,b), w in current_nodes:
        for (x,y), v in pairs:
            