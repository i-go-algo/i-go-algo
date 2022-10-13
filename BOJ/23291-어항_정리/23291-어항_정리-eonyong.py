import sys
from collections import deque

input = sys.stdin.readline


def FeedFish(fishes):
    visited = [[0] * len(fish) for fish in fishes]
    for row in range(len(fishes)):
        for col in range(len(fishes[row])):
            for j, i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nj, ni = row + j, col + i
                if 0 <= nj < len(fishes) and 0 <= ni < len(fishes[nj]):
                    abs_val = (fishes[row][col] - fishes[nj][ni]) // 5
                    if abs_val > 0:
                        visited[nj][ni] += abs_val
                        visited[row][col] -= abs_val

    # 동시에 일어난 어항의 변화를 적용시켜줌
    for row in range(len(fishes)):
        for col in range(len(fishes[row])):
            fishes[row][col] += visited[row][col]

    return fishes


def MakeOneLine(boards):
    boards = [deque(board) for board in boards]
    tmp = []
    while len(tmp) != n:
        for row in range(len(boards) - 1, -1, -1):
            if boards[row]:
                tmp.append(boards[row].popleft())
    else:
        return tmp


n, k = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0

while True:
    bowls = []
    # 값 비교해서 k보다 작거나 같으면 아웃
    # 그게 아니면 가 장 작은 어항에 물고기 1씩 추가
    ls_min, ls_max = min(ls), max(ls)
    if ls_max - ls_min <= k: break
    else:
        cnt += 1
        for idx in range(n):
            ls[idx] += 1 if ls[idx] == ls_min else 0

    # 공중부양 수행하는데 가장 아랫단의 어항보다
    # 공중부양 어항의 길이가 길면 나온다
    while True:
        length = len(bowls[0]) if bowls else 1
        tmp, remains = ls[:length], ls[length:]
        bowls.append(tmp)
        ls = remains[:]
        if bowls and len(bowls) > len(ls):
            bowls.pop()
            bowls.append(tmp + remains)
            break
        bowls = list(map(list, zip(*bowls[::-1])))

    # 인접한 물고기 주고 받기
    bowls = FeedFish(bowls)

    # 한 줄로 만드는 행위
    bowls = MakeOneLine(bowls)

    # 그림 9 만드는 법
    lft, rgt = bowls[:n // 2][::-1], bowls[n // 2:]
    bowls = [lft, rgt]

    # 그림 10 만드는 법
    tmp = deque([])
    for row in range(2):
        tmp.appendleft(bowls[row][:n // 4][::-1])
        tmp.append(bowls[row][n // 4:])
    bowls = list(tmp)

    # 인접한 물고기에게 밥주는 행위
    bowls = FeedFish(bowls)

    # 한 줄로 만드는 행위
    ls = MakeOneLine(bowls)

print(cnt)
