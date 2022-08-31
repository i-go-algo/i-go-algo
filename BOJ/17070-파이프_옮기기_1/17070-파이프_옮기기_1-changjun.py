# git commit -m "submit : BOJ 17070 파이프 옮기기 1 (changjun)"

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
cnt = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
cnt[0][1][0] = 1

for i in range(n):
    for j in range(1, n):

        if j + 1 < n and grid[i][j + 1] == 0:
            cnt[i][j + 1][0] = cnt[i][j + 1][0] + cnt[i][j][0]
            cnt[i][j + 1][0] = cnt[i][j + 1][0] + cnt[i][j][2]
        if i + 1 < n and grid[i + 1][j] == 0:
            cnt[i + 1][j][1] = cnt[i + 1][j][1] + cnt[i][j][1]
            cnt[i + 1][j][1] = cnt[i + 1][j][1] + cnt[i][j][2]
        if i + 1 < n and j + 1 < n and grid[i + 1][j + 1] == 0 and grid[i + 1][j] == 0 and grid[i][j + 1] == 0:
            cnt[i + 1][j + 1][2] = cnt[i + 1][j + 1][2] + cnt[i][j][0]
            cnt[i + 1][j + 1][2] = cnt[i + 1][j + 1][2] + cnt[i][j][1]
            cnt[i + 1][j + 1][2] = cnt[i + 1][j + 1][2] + cnt[i][j][2]
answer = sum(cnt[-1][-1])
print(answer)
