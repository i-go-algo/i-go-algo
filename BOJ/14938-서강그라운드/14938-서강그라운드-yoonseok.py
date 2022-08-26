# git commit -m "submit : BOJ 14938 서강그라운드 (yoonseok)"
n, m, r = map(int,input().split())
items = list(map(int,input().split()))
field = [[987654321]*n for i in range(n)]

for i in range(r):
    i,j,dis = map(int,input().split())
    field[i-1][j-1] = dis
    field[j-1][i-1] = dis
for k in range(n):
    for i in range(n):
        for j in range(n):
            if field[i][j] > field[i][k]+field[k][j]:
                field[i][j] = field[i][k]+field[k][j]
max_items = 0

for i in range(n):
    temp = items[i]
    for j in range(n):
        if field[i][j] <= m:
            temp+=items[j]
    max_items = max(max_items,temp)
print(max_items)