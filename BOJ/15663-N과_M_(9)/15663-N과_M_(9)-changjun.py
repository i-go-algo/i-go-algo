# git commit -m "submit : BOJ 15663 N과 M (9) (changjun)"

from itertools import permutations

n, m = map(int,input().split())

lst = list(map(int,input().split()))

combi = sorted(list(set(permutations(lst, m))))

for nums in combi:
    print(*nums)