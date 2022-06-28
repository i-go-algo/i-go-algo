# git commit -m "submit : BOJ 01463 1로 만들기 (yoonseok)"
INF = 10000001
N = int(input())
count = [INF]*(N+1)
count[1] = 0
for i in range(2,N+1):
    if(i%3==0):
        count[i]=min(count[i],count[i//3]+1)
    if(i%2==0):
        count[i]=min(count[i],count[i//2]+1)
    count[i] = min(count[i],count[i-1]+1)
print(count[N])
    