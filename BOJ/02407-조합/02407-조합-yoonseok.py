# git commit -m "submit : BOJ 02407 조합 (yoonseok)"
M, N = map(int,input().split())
combs = [[1]*101 for i in range(101)]
for i in range(1,101):
    for j in range(1,i+1):
        combs[i][j] = combs[i-1][j-1]+combs[i-1][j]

print(combs[M-1][N])