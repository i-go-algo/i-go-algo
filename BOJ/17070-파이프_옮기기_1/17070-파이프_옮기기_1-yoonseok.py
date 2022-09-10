# git commit -m "submit : BOJ 17070 파이프 옮기기 1 (yoonseok)"
import sys
input = sys.stdin.readline
N = int(input())
house = [list(map(int,input().split())) for i in range(N)]
count = 0
dp = [[[0]*3 for i in range(N)] for j in range(N)]

dp[0][1][0] = 1
for i in range(2,N):
    if house[0][i]==0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1,N):
    for j in range(1,N):
        if house[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j-1][0]+dp[i][j-1][2]
        dp[i][j][1] = dp[i-1][j][1]+dp[i-1][j][2]
        if house[i][j-1]==0 and house[i-1][j]==0:
            dp[i][j][2] = dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]
print(sum(dp[N-1][N-1]))
# def dfs(i,j,dir):
#     global count
#     if i==N-1 and j==N-1:
#         count+=1
#         return
#     if dir==0 or dir==2:
#         if j+1<N and house[i][j+1]==0:
#             dfs(i,j+1,0)
#         if (dir == 1 or dir == 2) and i+1<N:
#             if house[i+1][j] == 0:
#                 dfs(i+1, j, 1)
#         if dir == 0 or dir == 1 or dir == 2:
#             if i + 1 < N and j + 1 < N:
#                 if house[i+1][j] == 0 and house[i][j+1] == 0 and house[i+1][j+1] == 0:
#                     dfs(i+1, j+1, 2)
# dfs(0,1,0)
# print(count)



