# git commit -m "submit : BOJ 02096 내려가기 (changjun)"

n = int(input())

lst = [list(map(int,input().split())) for _ in range(n)]

x, y, z = lst[0]
a, b, c = lst[0]
for i, j, k in lst[1:]:
    x, y, z = i + min(x,y), j + min(x,y,z), k + min(y,z)
    a, b, c = i + max(a,b), j + max(a,b,c), k + max(b,c)

print(max(a,b,c), min(x,y,z))
