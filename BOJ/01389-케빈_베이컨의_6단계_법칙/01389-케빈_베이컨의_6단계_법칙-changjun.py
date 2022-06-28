# git commit -m "submit : BOJ 01389 케빈 베이컨의 6단계 법칙 (changjun)"

from collections import defaultdict, deque
n, m = map(int,input().split())

dic = defaultdict(set)

for _ in range(m):
    a, b = map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)

res = []

for i in range(1, n+1):
    q = deque()
    q.append((i, 0))

    visited = set()
    visited.add(i)

    ans = 0

    while q:
        node, dist = q.popleft()
        ans += dist

        for tmp in dic[node]:
            if tmp not in visited:
                visited.add(tmp)
                q.append((tmp, dist + 1))
                
    res.append(ans)

print(res.index(min(res)) + 1)



