# git commit -m "submit : BOJ 01806 부분합 (yoonseok)"
N, S = map(int,input().split())
nums = list(map(int,input().split()))+[0]
i = 0
j = 0
ans = 200000
pos = False
sm = nums[0]
while j < N and i<=j:
    if sm==S:
        ans = min(ans,j-i+1)
        j+=1
        sm+=nums[j]
        pos = True
    elif sm < S:
        j+=1
        sm+=nums[j]
    else:
        pos = True
        ans = min(ans,j-i+1)
        sm-=nums[i]
        i+=1
if pos:
    print(ans)
else:
    print(0)