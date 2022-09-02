# git commit -m "submit : BOJ 15686 치킨 배달 (changjun)"

from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

house = set()
chicken = deque()

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            house.add((i, j))
        elif lst[i][j] == 2:
            chicken.append((i, j))

l = len(chicken)
dic = dict()
res = 2147483647
for x, y in house:
    dic[(x, y)] = [0] * l

    for i in range(l):
        dic[(x, y)][i] = abs(chicken[i][0] - x) + abs(chicken[i][1] - y)

if m == l:
    queue = [list(range(l))]
else:
    queue = deque()
    queue.append([])

    while 1:
        if len(queue[0]) == m:

            break

        tmp = queue.popleft()

        if tmp:
            M = max(tmp)

        for i in range(l):
            if tmp and i <= M:
                continue
            queue.append(tmp + [i])


for use in queue:
    tmp_res = 0
    for value in dic.values():
        tmp_res += min([value[i] for i in range(l) if i in use])
    if res > tmp_res:
        res = tmp_res

print(res)
