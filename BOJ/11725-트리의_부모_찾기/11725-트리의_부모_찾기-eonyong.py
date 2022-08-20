# git commit -m "submit : BOJ 11725 트리의 부모 찾기 (eonyong)"
def WhereMyParents(nodes, trees, parents):
    while nodes:
        nexts = []
        for node in nodes:
            for tree in trees[node]:
                if not parents[tree]:
                    parents[tree] = node
                    nexts.append(tree)
        nodes = nexts[:]
    return parents[2:]


n = int(input())
trees = [[] for _ in range(n + 1)]
parents = [1] * 2 + [0] * (n - 1)
for _ in range(n - 1):
    s, e = map(int, input().split())
    trees[s].append(e)
    trees[e].append(s)

for parent in WhereMyParents([1], trees, parents):
    print(parent)
