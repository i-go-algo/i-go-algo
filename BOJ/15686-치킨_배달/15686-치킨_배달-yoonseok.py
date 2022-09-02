# git commit -m "submit : BOJ 15686 치킨 배달 (yoonseok)"
from itertools import combinations
N, M = map(int,input().split())
city = [list(map(int,input().split())) for i in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        if city[i][j] == 2:
            chicken.append((i,j))
def cal(chic, house):
    res = 0
    for h in house:
        temp = 987654321
        for c in chic:
            temp = min(temp, abs(h[0]-c[0])+abs(h[1]-c[1]))
        res+=temp
    return res

combs = list(combinations(chicken,M))
temp = 987654321

for chic in combs:
    
    temp = min(temp,cal(chic,house))
print(temp)
    
