from collections import deque


def bfs():
    queue = deque([n])

    while queue:
        cur = queue.popleft()

        if cur == k:
            print(dist[cur])
            break

        for nx in (cur - 1, cur + 1, cur * 2):
            if 0 <= nx <= maximum and not dist[nx]:
                dist[nx] = dist[cur] + 1
                queue.append(nx)


n, k = map(int, input().split())
maximum = 10 ** 5
dist = [0] * (maximum + 1)

bfs()
