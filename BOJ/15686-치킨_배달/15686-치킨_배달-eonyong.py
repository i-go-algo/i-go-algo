# git commit -m "submit : BOJ 15686 치킨 배달 (eonyong)"
from itertools import combinations

N, M = map(int, input().split())
house, chickens = [], []
answer = 100000000
for row in range(N):
    arr = list(map(int, input().split()))
    for col in range(N):
        if arr[col] == 1:
            house.append([row, col])
        if arr[col] == 2:
            chickens.append([row, col])

for chicken in combinations(chickens, M):
    total = 0
    for r, c in house:
        distance = N ** 2
        for s, e in chicken:
            distance = abs(s - r) + abs(e - c) if distance >= abs(s - r) + abs(e - c) else distance
        total += distance
    if answer > total:
        answer = total
print(answer)