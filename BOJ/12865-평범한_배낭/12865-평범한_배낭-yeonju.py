n, k = map(int, input().split())
stuff = [[0, 0]]
for i in range(n):
    stuff.append(list(map(int, input().split())))

knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j - weight] + value, knapsack[i - 1][j])

print(knapsack[n][k])
