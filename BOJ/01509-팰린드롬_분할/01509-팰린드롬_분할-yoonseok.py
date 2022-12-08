# git commit -m "submit : BOJ 01509 팰린드롬 분할 (yoonseok)"
s = input()
n = len(s)
palin = [[False]*(n+1) for _ in range(n+1)]
dp = [987654321]*(n+1)
s = " "+s
for i in range(1,n+1):
    palin[i][i]=True
for i in range(1,n):
    palin[i][i+1]=(s[i]==s[i+1])
for j in range(2,n):
    for i in range(1,n-j+1):
        if s[i]==s[i+j] and palin[i+1][i+j-1]:
            palin[i][i+j]=1
dp[0]=0
for i in range(1,n+1):
    for j in range(1,i+1):
        if palin[j][i]:
            dp[i]=min(dp[i],dp[j-1]+1)
print(dp[n])