# git commit -m "submit : BOJ 11404 플로이드 (eonyong)"
n, m = [int(input()) for _ in range(2)]
dist = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    dist[s - 1][e - 1] = min(dist[s - 1][e - 1], w)


for start in range(n):
    for middle in range(n):
        for end in range(n):
            dist[middle][end] = min(dist[middle][end], dist[middle][start] + dist[start][end])

for row in range(n):
    for col in range(n):
        if dist[row][col] == float('inf') or row == col:
            dist[row][col] = 0
    else:
        print(*dist[row])