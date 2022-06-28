# git commit -m "submit : BOJ 01260 DFS와 BFS (changjun)"

n, m, v = map(int,input().split())

from collections import defaultdict, deque

dic = defaultdict(set)

for _ in range(m):
    s, e = map(int,input().split())

    dic[s].add(e)
    dic[e].add(s)

for key, val in dic.items():
    dic[key] = sorted(val)

dfs = deque()
bfs = deque()

bfs.append(v)
dfs.append(v)

bfs_visited = set()
dfs_visited = set()

bfs_visited.add(v)
dfs_visited.add(v)

dfs_ans = deque()
bfs_ans = deque()

dfs_ans.append(v)
while dfs:
    tmp = dfs[-1]
    for node in dic[tmp]:
        if node not in dfs_visited:
            dfs_ans.append(node)
            dfs_visited.add(node)
            dfs.append(node)
            break
    else:
        dfs.pop()

while bfs:
    tmp = bfs.popleft()
    bfs_ans.append(tmp)
    for node in dic[tmp]:
        if node not in bfs_visited:
            bfs_visited.add(node)
            bfs.append(node)

print(*dfs_ans)
print(*bfs_ans)

