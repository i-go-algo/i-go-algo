# git commit -m "submit : BOJ 02630 색종이 만들기 (yoonseok)"
ans = [0,0]
N = int(input())
paper = [list(map(int,input().split())) for i in range(N)]
def counting(N,x,y):
    global paper
    check = True
    target = paper[x][y]
    for i in range(N):
        for j in range(N):
            if paper[x+i][y+j]!=target:
                check = False
    if check:
        ans[target]+=1
    else:
        counting(N//2,x,y)
        counting(N//2,x,(2*y+N)//2)
        counting(N//2,(2*x+N)//2,y)
        counting(N//2,(2*x+N)//2,(2*y+N)//2)
counting(N,0,0)
print(ans[0])
print(ans[1])


