import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m, z = map(int, input().split())
    
arr = [list(map(int, input().split())) for _ in range(n)]

score = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            q = deque([[i, j]])
            visited[i][j] = 1
            val = 1
            coordinate = [(i, j)]
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                        visited[nx][ny] = 1
                        val += 1
                        coordinate.append((nx, ny))
                        q.append([nx, ny])
            for x, y in coordinate:
                score[x][y] = arr[x][y] * val

dice = [2, 1, 5, 6, 4, 3]  
down = [0, 6, 5, 4, 3, 2, 1]
ans = 0
arrow = 0  
x, y = 0, 0
nx, ny = 0, 0

for _ in range(z):
    x, y = nx, ny
    nx, ny = x + dx[arrow], y + dy[arrow]
    if not (0 <= nx < n and 0 <= ny < m): 
        arrow = (arrow + 2) % 4
        nx, ny = x + dx[arrow], y + dy[arrow]

    ans += score[nx][ny]

    if arrow == 0: 
        dice[4], dice[1], dice[5], dice[3] = dice[3], dice[4], dice[1], dice[5]
    if arrow == 1: 
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    if arrow == 2:
        dice[4], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[4]
    if arrow == 3: 
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

    if dice[3] > arr[nx][ny]: 
        arrow = (arrow + 1) % 4
    if dice[3] < arr[nx][ny]: 
        arrow = (arrow + 3) % 4

print(ans)
