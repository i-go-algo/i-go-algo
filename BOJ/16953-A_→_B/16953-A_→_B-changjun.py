# git commit -m "submit : BOJ 16953 A → B (changjun)"

from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((a, 1))

while q:
    num, cnt = q.popleft()
    cnt += 1

    tmp = num * 2
    if tmp == b:
        print(cnt)
        break
    if tmp < b:
        q.append((tmp, cnt))

    tmp = num * 10 + 1
    if tmp == b:
        print(cnt)
        break
    if tmp < b:
        q.append((tmp, cnt))
else:
    print(-1)
