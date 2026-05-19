import sys
from typing import List
import time

characters = sys.stdin.buffer.readline().decode().strip().replace(" ", "")

data = sys.stdin.buffer.read().split()


cost_pair = []
idx = 0
length  = len(characters)

for n in range(length):
    row = [int(p) for p in data[idx: idx + length]]
    idx += length
    cost_pair.append(row)

number_queries = int(data[idx]); idx += 1

list_queries = []

for n in range(number_queries):
    list_queries.append((data[idx].decode(), data[idx+1].decode()))
    idx += 2

def doing_stuff(cost_pair: List, characters: str, query: tuple[str, str]) -> str:
    charindex = {c: i for i, c in enumerate(characters)}
    s1 = query[0]
    s2 = query[1]
    m = len(s1)
    n = len(s2)

    trace =  [[""] * (n+1) for _ in range(m+1)]
    dp = [[0] * (n+1) for _ in range(m+1)]



    for i in range(m+1):
        dp[i][0] = i*-4

    for j in range(n+1):
        dp[0][j] = j*-4

    for i in range (1, m+1):
        for j in range(1, n+1):
            diag = dp[i-1][j-1]+ cost_pair[charindex[s1[i-1]]][charindex[s2[j-1]]]
            up   = dp[i-1][j] - 4
            left = dp[i][j-1] - 4

            best = max(diag,up,left)

            dp[i][j] = best

            if best == diag:
                trace[i][j] = "diag"
            elif best == up:
                trace[i][j] = "up"
            elif best == left:
                trace[i][j] = "left"

    r1 = ""
    r2 = ""
    while m > 0 or n > 0:

        if m > 0 and n > 0 and trace[m][n] == "diag":
            r1 += s1[m-1]
            r2 += s2[n-1]
            m -= 1
            n -= 1
        elif m > 0 and (n == 0 or trace[m][n] == "up"):
            r1 += s1[m-1]
            r2 += "*"
            m -= 1
        elif n > 0 and (m == 0 or trace[m][n] == "left"):
            r1 += "*"
            r2 += s2[n-1]
            n -= 1


            
    return "".join(reversed(r1))+ " " + "".join(reversed(r2))


def doing_stuff_3(cost_pair: List, characters: str, query: tuple[str, str]) -> str:
    charindex = {c: i for i, c in enumerate(characters)}
    res1 = ""
    res2 = ""
    s1 = query[0]
    s2 = query[1]
    m = len(s1)
    n = len(s2)

    dp = [
        [[0, ["", ""]] for _ in range(n+1)]
        for _ in range(m+1)
    ]


    for i in range(1, m+1):
        dp[i][0][0] = i*-4
        dp[i][0][1][0] = s1[:i]
        dp[i][0][1][1] = "*"*i


    for j in range(1, n+1):
        dp[0][j][0] = j*-4
        dp[0][j][1][0] = "*"*j
        dp[0][j][1][1] = s2[:j]

    for i in range (1, m+1):
        for j in range(1, n+1):
            diag = dp[i-1][j-1][0] + cost_pair[charindex[s1[i-1]]][charindex[s2[j-1]]]
            up   = dp[i-1][j][0] - 4
            left = dp[i][j-1][0] - 4

            best = max(diag,left,up)

            dp[i][j][0] = best

            if best == diag:
                dp[i][j][1][0] = dp[i-1][j-1][1][0] + s1[i-1]
                dp[i][j][1][1] = dp[i-1][j-1][1][1] + s2[j-1]
            elif best == up:
                dp[i][j][1][0] = dp[i-1][j][1][0] + s1[i-1]
                dp[i][j][1][1] = dp[i-1][j][1][1] + "*"
            elif best == left:
                dp[i][j][1][0] = dp[i][j-1][1][0] + "*"
                dp[i][j][1][1] = dp[i][j-1][1][1] + s2[j-1]
                



    return dp[m][n][1][0] + " " + dp[m][n][1][1]

for p in list_queries:
    start = time.time()

    for p in list_queries:
        print(doing_stuff(cost_pair, characters, p))

    end = time.time()

    print("Time:", end - start, "seconds", file=sys.stderr)

