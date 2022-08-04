# git commit -m "submit : BOJ 02638 치즈 (eonyong)"
from collections import defaultdict

def happyCheeze(boards, visited, n, m):
    boundary, edges, getRidOf = defaultdict(int), [[0, 0]], []
    while edges:
        nxt_edges = []
        for y, x in edges:
            for j, i in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nj, ni = y + j, x + i
                if 0 <= nj < n and 0 <= ni < m and not visited[nj][ni]:
                    if boards[nj][ni]:
                        boundary[(nj, ni)] += 1
                    else:
                        visited[nj][ni] = True
                        nxt_edges.append([nj, ni])
        edges = nxt_edges[:]

    for k, v in boundary.items():
        if v >= 2:
            getRidOf.append(k)
    return getRidOf


n, m = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(n)]
days = 0
while True:
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    winds = happyCheeze(boards, visited, n, m)
    if not winds:
        break
    else:
        for row, col in winds:
            boards[row][col] = 0
    days += 1
print(days)