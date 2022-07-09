# git commit -m "submit : BOJ 01697 숨바꼭질 (changjun)"

from collections import deque

n, m = map(int,input().split())

q = deque()

q.append((n, 0))

visited = set()
visited.add(n)

while q:
    now, time = q.popleft()
    if now == m:
        print(time)
        break
    lst = [now-1, now+1, now*2]
    for i in lst:
        if 0<=i <= 100000 and i not in visited:
            visited.add(i)
            q.append((i, time+1))
