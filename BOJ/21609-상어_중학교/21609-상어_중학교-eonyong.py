# git commit -m "submit : BOJ 21609 상어 중학교 (eonyong)"
import sys
from collections import deque

input = sys.stdin.readline


def BFS(r, c, n, boards, visited):
    temp = deque()
    temp.append((r, c))
    groups = [(r, c, boards[r][c])]
    cnt = 0
    while temp:
        row, col = temp.pop()
        for j, i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nj, ni = row + i, col + j
            if 0 <= nj < n and 0 <= ni < n and not visited[nj][ni] and (not boards[nj][ni] or boards[r][c] == boards[nj][ni]):
                visited[nj][ni] = True
                if not boards[nj][ni]:
                    cnt += 1
                groups.append((nj, ni, boards[nj][ni]))
                temp.append((nj, ni))
    groups.sort(key=lambda x: (-x[2], x[0], x[1]))
    if len(groups) >= 2:
        return groups, cnt
    else:
        return [], cnt


n, m = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(n)]
answer = 0

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    zero_cnt, group = 0, {}
    for row in range(n):
        for col in range(n):
            if boards[row][col] > 0 and not visited[row][col]:
                visited[row][col] = True
                temp_group, cnt = BFS(row, col, n, boards, visited)
                for y, x, color in temp_group:
                    if not color:
                        visited[y][x] = False
                if not group:
                    group, zero_cnt = temp_group, cnt
                else:
                    if len(temp_group) >= 2:
                        if len(group) < len(temp_group):
                            group, zero_cnt = temp_group, cnt
                        elif len(group) == len(temp_group):
                            # 0의 갯수가 적거나
                            if cnt > zero_cnt:
                                group, zero_cnt = temp_group, cnt 
                            elif cnt == zero_cnt:
                                if group[0][0] < temp_group[0][0] or (group[0][0] == temp_group[0][0] and group[0][1] < temp_group[0][1]):
                                    group, zero_cnt = temp_group, cnt
    if len(group) < 2:
        break
    answer += len(group) ** 2
    for y, x, color in group:
        boards[y][x] = -2

    for i in range(n - 2, -1, -1):  # 밑에서 부터 체크
        for j in range(n):
            if boards[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0 <= r + 1 < n and boards[r + 1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        boards[r + 1][j] = boards[r][j]
                        boards[r][j] = -2
                        r += 1
                    else:
                        break

    boards = list(reversed(list(map(list, zip(*boards)))))[:]

    for i in range(n - 2, -1, -1):
        for j in range(n):
            if boards[i][j] > -1:
                r = i
                while True:
                    if 0 <= r + 1 < n and boards[r + 1][j] == -2:
                        boards[r + 1][j] = boards[r][j]
                        boards[r][j] = -2
                        r += 1
                    else:
                        break
print(answer)
