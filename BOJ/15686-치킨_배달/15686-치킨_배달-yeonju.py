import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

chickens = []
houses = []
res = 1e9

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chickens.append((i, j))
        elif arr[i][j] == 1:
            houses.append((i, j))

for selected_chickens in combinations(chickens, m):
    temp_total = 0
    for house in houses:
        r1, c1 = house
        cur_dist = 1e9
        for chicken in selected_chickens:
            r2, c2 = chicken
            cur_dist = min(cur_dist, abs(r1 - r2) + abs(c1 - c2))
        temp_total += cur_dist
    res = min(res, temp_total)

print(res)
