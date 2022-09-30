# git commit -m "submit : BOJ 16234 인구 이동 (eonyong)"
from collections import deque
import sys
input = sys.stdin.readline

n, left, right = map(int, input().split())
boundary = [list(map(int, input().split())) for _ in range(n)]
days = 0
while True:
    answer = []
    visited = [[False] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                neighbors, updates, cnt, val = deque([[row, col]]), [[row, col]], 1, boundary[row][col]
                # 이웃과 이동하는지 확인하는 func
                while neighbors:
                    r, c = neighbors.popleft()
                    visited[r][c] = True
                    for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        nj, ni = r + j, c + i
                        if 0 <= nj < n and 0 <= ni < n and not visited[nj][ni] and left <= abs(boundary[r][c] - boundary[nj][ni]) <= right:
                            visited[nj][ni] = True
                            updates.append([nj, ni])
                            cnt += 1
                            val += boundary[nj][ni]
                            neighbors.append([nj, ni])
                # 서로 이동할 경우
                if cnt != 1:
                    updates.append(val // cnt)
                    answer.append(updates)
    # 이동하는 사람이 있는 경우, 이동 후 days + 1
    if answer:
        while answer:
            ans = answer.pop()
            people = ans.pop()
            for y, x in ans:
                boundary[y][x] = people
        days += 1
    # 없으면 while 탈출
    else:
        break
print(days)