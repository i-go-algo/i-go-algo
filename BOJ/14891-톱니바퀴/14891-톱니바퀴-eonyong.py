# git commit -m "submit : BOJ 14891 톱니바퀴 (eonyong)"
from collections import deque

def f(n, d, i):
    if 0 <= n + i < 4 and d:
        if (i == -1 and rails[n][6] != rails[n + i][2]) or (i == 1 and rails[n][2] != rails[n + i][6]):
            f(n + i, -d, i)
            rails[n + i].rotate(-d)

rails = [deque(list(input())) for _ in range(4)]
answer = 0

for _ in range(int(input())):
    num, rot = map(int, input().split())
    f(num - 1, rot, 1)
    f(num - 1, rot, -1)
    rails[num - 1].rotate(rot)

for i in range(4):
    if rails[i][0] == '1':
        answer += 2 ** i

print(answer)