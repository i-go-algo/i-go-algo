import heapq

n, m = map(int, input().split())

infos = [[] for _ in range(n + 1)]
levels = [0 for _ in range(n + 1)]
queue = []
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    infos[a].append(b)
    levels[b] += 1

for i in range(1, n + 1):
    if levels[i] == 0:
        heapq.heappush(queue, i)

while queue:
    temp = heapq.heappop(queue)
    ans.append(temp)

    for i in infos[temp]:
        levels[i] -= 1
        if levels[i] == 0:
            heapq.heappush(queue, i)

print(' '.join(map(str, ans)))
