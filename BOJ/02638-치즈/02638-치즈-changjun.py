# git commit -m "submit : BOJ 02638 치즈 (changjun)"
from collections import deque, defaultdict

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

flag = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
tmp = -1
while flag:
    tmp += 1
    flag = 0
    q = deque()
    q.append((0, 0))
    visited = set()
    visited.add((0, 0))
    dic = defaultdict(int)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if lst[nx][ny] == 0 and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
                elif lst[nx][ny] == 1:
                    dic[(nx, ny)] += 1
                    flag = 1
    for key, value in dic.items():
        if value >= 2:
            x, y = key
            lst[x][y] = 0
print(tmp)
