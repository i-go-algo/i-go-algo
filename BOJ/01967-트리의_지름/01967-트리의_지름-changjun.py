# git commit -m "submit : BOJ 01967 트리의 지름 (changjun)"

from collections import defaultdict, deque
n = int(input())

dic = defaultdict(set)
for _ in range(n-1):
    s, e, w = map(int,input().split())
    dic[s].add((e,w))
    dic[e].add((s,w))


lst = [-1]*(n+1)

lst[1] = 0
q = deque()
q.append(1)
while q:
    node = q.popleft()
    for new_node, new_distance in dic[node]:
        if lst[new_node] == -1:
            lst[new_node] = new_distance + lst[node]
            q.append(new_node)

max_node = lst.index(max(lst))

lst = [-1]*(n+1)

lst[max_node] = 0
q = deque()
q.append(max_node)
while q:
    node = q.popleft()
    for new_node, new_distance in dic[node]:
        if lst[new_node] == -1:
            lst[new_node] = new_distance + lst[node]
            q.append(new_node)
print(max(lst))