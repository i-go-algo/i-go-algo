# git commit -m "submit : BOJ 11053 가장 긴 증가하는 부분 수열 (yoonseok)"
N = int(input())
arr = list(map(int,input().split()))
check = [1001] * (N+1)
check[0]=0
ans = 0
now = 0
for num in arr:
    if num > now:
        ans+=1
        check[ans]=num
        now = num
    else :
        l = 0
        r = ans
        while l<=r:
            mid = (l+r)//2
            if check[mid] <num:
                l = mid+1
            else:
                r = mid-1
        check[l] = num
        if l == ans : 
            now = num
    #print(check, now)

print(ans)
