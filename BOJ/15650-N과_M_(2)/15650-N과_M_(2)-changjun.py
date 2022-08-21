# git commit -m "submit : BOJ 15650 N과 M (2) (changjun)"

from itertools import combinations

n, m = map(int,input().split())

for nums in combinations(range(1,n+1),m):
    print(*nums)