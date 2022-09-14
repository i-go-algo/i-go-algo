# git commit -m "submit : BOJ 14501 퇴사 (yoonseok)"
N = int(input())
table = []
dp = []
for i in range(N):
    table.append(list(map(int,input().split())))  
    dp.append(table[i][1])
dp.append(0)

for i in range(N-1,-1,-1):
    if table[i][0]+i>N:
        dp[i] = dp[i+1]
    else:
        dp[i]=max(dp[i+1],table[i][1]+dp[i+table[i][0]])
print(dp[0])


