# git commit -m "submit : BOJ 01043 거짓말 (changjun)"

n, m = map(int,input().split())
true_num, *true_lst = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(m)]

parent = dict()
for i in range(1, n+1):
    parent[i] = i

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x,y):
    tmp_x = find(x)
    tmp_y = find(y)
    if tmp_x != tmp_y:
        parent[tmp_x] = tmp_y


for tmp_num, *tmp_lst in lst:
    for i in range(len(tmp_lst)-1):
        union(tmp_lst[i],tmp_lst[i+1])


true_set = set()
for i in true_lst:
    true_set.add(find(i))

who_know_true = set()

for i in range(1, n+1):
    parent[i] = find(i)
    if parent[i] in true_set:
        who_know_true.add(parent[i])

ans = 0
for tmp_num, *tmp_lst in lst:
    for i in tmp_lst:
        if parent[i] in who_know_true:
            break
    else:
        ans += 1

print(ans)