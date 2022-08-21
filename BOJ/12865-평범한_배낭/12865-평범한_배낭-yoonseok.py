# git commit -m "submit : BOJ 12865 평범한 배낭 (yoonseok)"
N, K = map(int,input().split())
knapsack = [[0]*(K+1) for i in range(N+1)]
item = [[0,0]]+[list(map(int,input().split())) for i in range(N)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >=item[i][0]:
            temp = knapsack[i-1][j-item[i][0]]+item[i][1]
            knapsack[i][j] = max(knapsack[i-1][j],temp)
        else:
            
            knapsack[i][j] = max(knapsack[i-1][j],knapsack[i][j-1])
print(knapsack[N][K])