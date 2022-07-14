# git commit -m "submit : BOJ 01931 회의실 배정 (changjun)"

n = int(input())

lst = [list(map(int,input().split())) for _ in range(n)]

lst = sorted(lst, key=lambda x : (x[1], x[0]))

res = 0
tmp = -1

for i in range(len(lst)):
    if lst[i][0] >= tmp:
        res += 1
            
        tmp = lst[i][1]

print(res)