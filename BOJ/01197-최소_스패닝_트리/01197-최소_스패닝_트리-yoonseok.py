# git commit -m "submit : BOJ 01197 최소 스패닝 트리 (yoonseok)"
v, e = map(int, input().split())
arr = []
for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append((c,a,b))

arr.sort(key=lambda x: x[0])
parent = list(range(v + 1))

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

sum = 0
for c, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        sum += c

print(sum)