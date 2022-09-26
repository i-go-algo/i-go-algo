# git commit -m "submit : BOJ 16234 인구 이동 (yoonseok)"
import math
from collections import deque

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, input().split())  # n*n, 인구차이 l명 이상, r명 이하

arr = list()
a_list = list()
for i in range(n):
    arr.append(list(map(int, input().split())))

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True

    union = [(i, j)]
    count = arr[i][j]  

    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r: 
                union.append((nx, ny))
                visit[nx][ny] = True
                dq.append((nx, ny))
                count += arr[nx][ny]

    for x, y in union:
        arr[x][y] = math.floor(count / len(union))

    return len(union)

result = 0 
while True: 
    visit = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:  
        break
    result += 1

print(result)