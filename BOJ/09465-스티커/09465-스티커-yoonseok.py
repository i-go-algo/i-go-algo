# git commit -m "submit : BOJ 09465 스티커 (yoonseok)"
T = int(input())
for tc in range(T):
    n = int(input())
    stickers = [list(map(int,input().split())) for i in range(2)]
    ans = [[0]*(n) for i in range(2)]
    ans[0][0] = stickers[0][0]
    ans[1][0] = stickers[1][0]
    for i in range(1,n):
       
        ans[0][i] = max(ans[1][i-1]+stickers[0][i],ans[0][i-1])
        ans[1][i] = max(ans[0][i-1]+stickers[1][i],ans[1][i-1])
    print(max(ans[0][n-1],ans[1][n-1]))
        
