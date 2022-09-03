# git commit -m "submit : BOJ 03190 뱀 (eonyong)"
from collections import deque
N = int(input())
board = [[0] * N for _ in range(N)]
swarm = deque([[0, 0]])

apple = int(input())
for _ in range(apple):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

rotation, idx = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0
rot_int, rot_cnt = int(input()), 0
rot = [list(input().split()) for _ in range(rot_int)]

cnt = 0
while True:
    head = swarm[-1][:]
    cnt += 1

    head[0], head[1] = head[0] + rotation[idx][0], head[1] + rotation[idx][1]

    if 0 <= head[0] < N and 0 <= head[1] < N:
        if head in swarm:
            break
        else:
            if not board[head[0]][head[1]]:
                swarm.append(head)
                swarm.popleft()
            else:
                board[head[0]][head[1]] = 0
                swarm.append(head)
    else:
        break

    if rot_cnt < rot_int and cnt == int(rot[rot_cnt][0]):
        idx = (idx - 1) % 4 if rot[rot_cnt][1] == 'L' else (idx + 1) % 4
        rot_cnt += 1

print(cnt)