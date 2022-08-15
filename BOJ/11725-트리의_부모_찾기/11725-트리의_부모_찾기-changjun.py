# git commit -m "submit : BOJ 11725 트리의 부모 찾기 (changjun)"
from collections import defaultdict, deque
n = int(input())
dic = defaultdict(set)
for _ in range(n-1):
    s, e = map(int,input().split())
    dic[s].add(e)
    dic[e].add(s)

lst = [0]*(n+1)

q = deque()
q.append(1)
lst[1] = 1

while q:
    x = q.popleft()
    for node in dic[x]:
        if not lst[node]:
            lst[node] = x
            q.append(node)

for i in range(2, n+1):
    print(lst[i])

