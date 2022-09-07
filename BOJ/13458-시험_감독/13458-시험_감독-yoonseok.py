# git commit -m "submit : BOJ 13458 시험 감독 (yoonseok)"
N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())
ans = 0
for i in range(N):
    ans += 1
    remain = A[i]-B
    if remain<=0:
        continue
    if remain%C:
        ans+=remain//C+1
    else:
        ans+=remain//C
print(ans)