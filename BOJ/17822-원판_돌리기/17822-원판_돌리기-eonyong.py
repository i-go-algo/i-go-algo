# git commit -m "submit : BOJ 17822 원판 돌리기 (eonyong)"
import sys
from collections import deque
input = sys.stdin.readline


n, m, t = map(int, input().split())
boards = deque(deque(list(map(int, input().split()))) for _ in range(n))
for _ in range(t):
    x, d, k = map(int, input().split())
    # d가 1이면 시계, 0이면 반시계
    direction = -1 if d else 1
    idx = x - 1
    # 각 배수에 있는 과녁을 k번 회전시키기
    while idx < n:
        for _ in range(k):
            boards[idx].rotate(direction)
        idx += x
    # 인접한 과녁이 있나 없나 파악하는 boolean 변수
    flag = False
    # 전체 합과 남아있는 수를 저장할 변수
    avg_val, cnt_val = 0, 0
    for row in range(n):
        for col in range(m):
            value = boards[row][col]
            # value가 0이 아니면
            if value:
                ls = deque()
                ls.append((row, col))
                
                avg_val += boards[row][col]
                cnt_val += 1
                # BFS를 통해 인접한 친구중에 같은 값을 가진 아이가 있는지 확인
                while ls:
                    y, x = ls.popleft()
                    for j, i in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        nj, ni = y + j, (x + i) % m
                        if 0 <= nj < n and value == boards[nj][ni]:
                            # 하나라도 바꾸면 flag를 건드려서 변한게 있다고 체크를 해준다.
                            flag = True
                            ls.append((nj, ni))
                            boards[nj][ni] = 0
                            
    # 인접한 게 하나도 없는 경우에 boards 안의 값을 업데이트
    if not flag:
        for row in range(n):
            for col in range(m):
                if boards[row][col]:
                    # 평균 / 사라지지 않은 값의 수 보다!! 크거나 작으면 값을 변경
                    if (avg_val / cnt_val) < boards[row][col]:
                        boards[row][col] -= 1
                    elif (avg_val / cnt_val) > boards[row][col]:
                        boards[row][col] += 1

print(sum(sum(board) for board in boards))
