# git commit -m "submit : BOJ 16953 A → B (eonyong)"
import sys


def GoToEnd(s, e, cnt):
    global answer
    if s == e:
        answer = min(answer, cnt)
    elif s < end:
        for m in [s * 2, 10 * s + 1]:
            GoToEnd(m, e, cnt + 1)


answer = float('inf')
start, end = map(int, sys.stdin.readline().split())
GoToEnd(start, end, 1)
print(answer) if answer != float('inf') else print(-1)