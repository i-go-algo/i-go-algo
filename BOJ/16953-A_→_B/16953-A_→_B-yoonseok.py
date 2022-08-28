# git commit -m "submit : BOJ 16953 A → B (yoonseok)"
from collections import deque
A,B = map(int,input().split())
q = deque()
q.append((A,1))
visited = dict()
visited[A]=True
flag = False
while q:
    now, times = q.popleft()
    if now==B:
        flag= True
        print(times)
        break
    else:
        if now*2<=B and not now*2 in visited:
            visited[now*2]=True
            q.append((now*2,times+1))
        if now*10+1<=B and not now*10+1 in visited:
            visited[now*10+1]=True
            q.append((now*10+1,times+1))
if not flag:
    print(-1)