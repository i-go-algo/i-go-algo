# git commit -m "submit : BOJ 01931 회의실 배정 (yoonseok)"
N = int(input())
time = []
for i in range(N):
    temp = list(map(int,input().split()))
    time.append(temp)

time.sort(key = lambda x : (x[1],x[0]))
ans = 1
now = time[0][1]
for i in range(N):
    if time[i][0]>=now:
        ans+=1
        now = time[i][1]

print(ans)