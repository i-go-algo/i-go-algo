# git commit -m "submit : BOJ 23291 어항 정리 (eonyong)"
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0

while True:
    bowls = []
    ls_max, ls_min = max(ls), min(ls)
    if ls_max - ls_min <= k:
        break
        # pass
    else:
        cnt += 1
        for idx in range(n):
            ls[idx] += 1 if ls[idx] == ls_min else 0
    while True:
        length = len(bowls[0]) if bowls else 1
        remains = []
        tmp, remains = ls[:length], ls[length:]
        bowls.append(tmp)
        ls = remains[:]
        if bowls and len(bowls) > len(ls):
            bowls.pop()
            bowls.append(tmp + remains)
            break
        bowls = list(map(list, zip(*bowls[::-1])))

    # 인접한 물고기 주고 받기
    H = len(bowls)
    visited = [[0] * len(bowl) for bowl in bowls]
    for row in range(H):
        for col in range(len(bowls[row])):
            for j, i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nj, ni = row + j, col + i
                if 0 <= nj < H and 0 <= ni < len(bowls[nj]):
                    abs_val = (bowls[row][col] - bowls[nj][ni]) // 5
                    if abs_val > 0:
                        visited[nj][ni] += abs_val
                        visited[row][col] -= abs_val
    for row in range(H):
        for col in range(len(bowls[row])):
            bowls[row][col] += visited[row][col]

    # 한 줄로 만드는 행위
    bowls = [deque(bowl) for bowl in bowls]
    tmp = []
    while len(tmp) != n:
        for row in range(len(bowls) - 1, -1, -1):
            if bowls[row]:
                tmp.append(bowls[row].popleft())
    else:
        bowls = tmp[:]

    # 그림 9 만드는 법
    lft, rgt = bowls[:n // 2][::-1], bowls[n // 2:]
    bowls = [lft, rgt]
    tmp = deque([])

    # 그림 10 만드는 법
    for row in range(2):
        lft, rgt = bowls[row][:n // 4][::-1], bowls[row][n // 4:]
        tmp.appendleft(lft)
        tmp.append(rgt)
    bowls = list(tmp)
    visited = [[0 for _ in range(len(bowls[0]))] for _ in range(len(bowls))]
    for row in range(len(bowls)):
        for col in range(len(bowls[row])):
            for j, i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nj, ni = row + j, col + i
                if 0 <= nj < len(bowls) and 0 <= ni < len(bowls[row]):
                    abs_val = (bowls[row][col] - bowls[nj][ni]) // 5
                    if abs_val > 0:
                        visited[nj][ni] += abs_val
                        visited[row][col] -= abs_val

    for row in range(len(bowls)):
        for col in range(len(bowls[row])):
            bowls[row][col] += visited[row][col]

    bowls = [deque(bowl) for bowl in bowls]
    tmp = []
    while len(tmp) != n:
        for row in range(len(bowls) - 1, -1, -1):
            if bowls[row]:
                tmp.append(bowls[row].popleft())
    else:
        ls = tmp[:]
print(cnt)
