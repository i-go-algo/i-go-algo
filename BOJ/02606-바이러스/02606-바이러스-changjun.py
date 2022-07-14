# git commit -m "submit : BOJ 02606 바이러스 (changjun)"

from collections import defaultdict, deque

n = int(input())
m = int(input())

dic = defaultdict(set)

for _ in range(m):
    x, y = map(int,input().split())

    dic[x].add(y)
    dic[y].add(x)

visited = set()
visited.add(1)

q = deque()
q.append(1)

while q:
    tmp = q.pop()
    for val in dic[tmp]:
        if val not in visited:
            visited.add(val)
            q.append(val)

print(len(visited) - 1)
