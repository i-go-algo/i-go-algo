import sys
from collections import deque
input = sys.stdin.readline


def bfs(cur):
    queue = deque()
    queue.append(cur)

    while queue:
        x = queue.popleft()

        if x == k:
            print(dist[x])
            break

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)


n, k = map(int, input().split())
dist = [0 for _ in range(100001)]
bfs(n)
