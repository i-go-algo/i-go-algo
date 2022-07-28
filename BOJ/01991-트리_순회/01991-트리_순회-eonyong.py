# git commit -m "submit : BOJ 01991 트리 순회 (eonyong)"
def pre_order(n):
    if n != '.':
        print(n, end='')
        pre_order(edge[n][0])
        pre_order(edge[n][1])


def in_order(n):
    if n != '.':
        in_order(edge[n][0])
        print(n, end='')
        in_order(edge[n][1])


def post_order(n):
    if n != '.':
        for v in edge[n]:
            post_order(v)
        print(n, end='')


from collections import defaultdict

V = int(input())
edge = defaultdict(list)

for _ in range(V):
    parent, *child = input().split()
    edge[parent] = child

pre_order('A')
print()
in_order('A')
print()
post_order('A')
