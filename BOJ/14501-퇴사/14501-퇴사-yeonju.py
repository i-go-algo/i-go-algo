n = int(input())
day_list = []
price_list = []

for _ in range(n):
    t, p = map(int, input().split())
    day_list.append(t)
    price_list.append(p)

dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + day_list[i] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(price_list[i] + dp[i + day_list[i]], dp[i + 1])

print(dp[0])
