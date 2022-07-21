# git commit -m "submit : BOJ 01149 RGB거리 (eonyong)"
n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
minRgb = [[float('inf')] * 3 for _ in range(n)]
for s in range(3):
    for e in range(3):
        if s != e:
            minRgb[1][e] = min(rgb[0][s] + rgb[1][e], minRgb[1][e])

for idx in range(2, n):
    for s in range(3):
        for e in range(3):
            if s != e:
                minRgb[idx][e] = min(minRgb[idx - 1][s] + rgb[idx][e], minRgb[idx][e])
print(min(minRgb[-1]))