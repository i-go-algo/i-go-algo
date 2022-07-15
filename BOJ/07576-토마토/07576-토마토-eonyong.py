# git commit -m "submit : BOJ 07576 토마토 (eonyong)"
m, n = map(int, input().split())
areas = []
tomatoes, zeroCnt = [], 0
visited = [[False for _ in range(m)] for _ in range(n)]
for row in range(n):
    r = list(map(int, input().split()))
    for col in range(m):
        if r[col] == 1:
            tomatoes.append([row, col])
            visited[row][col] = True
        elif not r[col]:
            zeroCnt += 1
    areas.append(r)
if len(tomatoes) == n * m:
    print(0)
else:
    days = -1
    while tomatoes:
        new_area = []
        for y, x in tomatoes:
            for j, i in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nj, ni = y + j, x + i
                if 0 <= nj < n and 0 <= ni < m and not visited[nj][ni] and not areas[nj][ni]:
                    visited[nj][ni] = True
                    zeroCnt -= 1
                    new_area.append([nj, ni])
        days += 1
        tomatoes = new_area[:]
    if not zeroCnt:
        print(days)
    else:
        print(-1)