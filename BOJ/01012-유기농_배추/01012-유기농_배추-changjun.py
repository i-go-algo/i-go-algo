# git commit -m "submit : BOJ 01012 유기농 배추 (changjun)"

from collections import deque

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for case in range(t):
    m, n, k = map(int,input().split())
    lst = [[0]*m for _ in range(n)]
    ans = 0

    bechu = set()

    for _ in range(k):
        j, i = map(int,input().split())
        lst[i][j] = 1


    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                ans += 1

                q = deque()
                q.append((i,j))

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 1:
                            lst[nx][ny] = 0
                            q.append((nx,ny))
    print(ans)

