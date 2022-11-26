strings = input()
n = len(strings)
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
res = [1e9 for _ in range(n + 1)]
res[0] = 0

for i in range(1, n + 1):
    dp[i][i] = 1

for i in range(1, n):
    if strings[i - 1] == strings[i]:
        dp[i][i + 1] = 1

for i in range(2, n):
    for j in range(1, n + 1 - i):
        if strings[j - 1] == strings[j + i - 1] and dp[j + 1][i + j - 1] == 1:
            dp[j][i + j] = 1

for i in range(1, n + 1):
    res[i] = min(res[i], res[i - 1] + 1)

    for j in range(i + 1, n + 1):
        if dp[i][j] != 0:
            res[j] = min(res[j], res[i - 1] + 1)

print(res[n])
