# git commit -m "submit : BOJ 14502 연구소 (eonyong)"
from collections import deque
import sys


def virusDiffusion(board, visited, viruses, w, h, two) -> int:
    virus = deque(viruses[:])
    cnt = 0
    while virus:
        r, c = virus.popleft()
        for j, i in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nj, ni = r + j, c + i
            if 0 <= nj < h and 0 <= ni < w and not board[nj][ni] and not visited[nj][ni]:
                visited[nj][ni] = True
                cnt += 1
                virus.append([nj, ni])
    else:
        return cnt + two


def buildTower(i, n, boards, visited, zeros, viruses, w, h, one, two):
    global answer
    if i == n:
        tf = [visit[:] for visit in visited]
        answer = max(w * h - (virusDiffusion(boards, tf, viruses, w, h, two) + one), answer)
    else:
        for y, x in zeros:
            if not boards[y][x]:
                boards[y][x] = 1
                buildTower(i + 1, n, boards, visited, zeros, viruses, w, h, one, two)
                boards[y][x] = 0


H, W = map(int, sys.stdin.readline().split())
boards, viruses, zeros, one, two = [], [], [], 0, 0
answer = 0
visited = [[False for _ in range(W)] for _ in range(H)]
for row in range(H):
    ls = list(map(int, sys.stdin.readline().split()))
    for col in range(W):
        if ls[col] == 2:
            visited[row][col] = True
            two += 1
            viruses.append([row, col])
        elif not ls[col]:
            zeros.append([row, col])
        else:
            one += 1
            visited[row][col] = True

    boards.append(ls)

buildTower(0, 3, boards, visited, zeros, viruses, W, H, one + 3, two)
print(answer)
