# git commit -m "submit : BOJ 23288 주사위 굴리기 2 (eonyong)"
import sys
from collections import deque

input = sys.stdin.readline

# d에 따른 추종 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 중복 값 갯수 찾기 위한 BFS 실행
def BFS(boards, r, c, n, m):
    ls = deque()
    cnt = 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    ls.append((r, c))
    visited[r][c] = True
    while ls:
        y, x = ls.popleft()
        for idx in range(4):
            nj, ni = y + dr[idx], x + dc[idx]
            if 0 <= nj < n and 0 <= ni < m and not visited[nj][ni] and boards[r][c] == boards[nj][ni]:
                visited[nj][ni] = True
                ls.append((nj, ni))
                cnt += 1
    return cnt


# 주사위 움직이는 방식
def DiceRotation(dices, d):
    if d == 0:
        dices[0], dices[2], dices[4], dices[5] = dices[2], dices[4], dices[5], dices[0]
    elif d == 1:
        dices[1], dices[2], dices[3], dices[5] = dices[5], dices[1], dices[2], dices[3]
    elif d == 2:
        dices[0], dices[2], dices[4], dices[5] = dices[5], dices[0], dices[2], dices[4]
    elif d == 3:
        dices[1], dices[2], dices[3], dices[5] = dices[2], dices[3], dices[5], dices[1]
    return dices


# 주사위 모양
dices = {0: 2, 1: 4, 2: 1, 3: 3, 4: 5, 5: 6}
n, m, k = map(int, input().split())

# 점수판 및 점수판 별 BFS 값
boards = [list(map(int, input().split())) for _ in range(n)]
cnt_boards = [[BFS(boards, row, col, n, m) for col in range(m)] for row in range(n)]
d = 1
row, col = 0, 0
answer = 0

for _ in range(k):

    # 주사위 위치 추종
    if not (0 <= row + dr[d] < n and 0 <= col + dc[d] < m):
        d = (d + 2) % 4

    # 정해진 방향으로 주사위 이동 및 주사위 회전
    row, col = row + dr[d], col + dc[d]
    dices = DiceRotation(dices, d)

    # boards의 값과 같은 것이 몇 개인지 찾고, 갯수 * boards[row][col]을 가산
    answer += cnt_boards[row][col] * boards[row][col]

    # 방향 전환 조건
    if dices[5] < boards[row][col]:
        d = (d - 1) % 4
    elif dices[5] > boards[row][col]:
        d = (d + 1) % 4

print(answer)
