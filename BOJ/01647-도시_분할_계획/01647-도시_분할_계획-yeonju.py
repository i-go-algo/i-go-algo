def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

parent = [i for i in range(n + 1)]

graph.sort()
res = []

for c, a, b in graph:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res.append(c)

print(sum(res[:-1]))
