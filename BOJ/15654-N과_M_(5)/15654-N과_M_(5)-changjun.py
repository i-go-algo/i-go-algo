# git commit -m "submit : BOJ 15654 N과 M (5) (changjun)"

from itertools import permutations

n, m = map(int,input().split())

lst = list(map(int,input().split()))
lst = sorted(lst)

for nums in permutations(lst, m):
    print(*nums)

